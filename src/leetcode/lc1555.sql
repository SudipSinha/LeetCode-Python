/* Bank Account Summary

Link: https://leetcode.com/problems/bank-account-summary/
 
Table: `Users`

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| user_id      | int     |
| user_name    | varchar |
| credit       | int     |
+--------------+---------+
`user_id` is the primary key (column with unique values) for this table.
Each row of this table contains the current credit information for each user.


Table: `Transactions`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| paid_by       | int     |
| paid_to       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
`trans_id` is the primary key (column with unique values) for this table.
Each row of this table contains information about the transaction in the bank.
User with id (`paid_by`) transfer money to user with id (`paid_to`).


Leetcode Bank (LCB) helps its coders in making virtual payments. Our bank records all transactions in the table `Transaction`, we want to find out the current balance of all users and check whether they have breached their credit limit (If their current credit is less than `0`).

Write a solution to report
*   `user_id`,
*   `user_name`,
*   `credit`, current balance after performing transactions, and
*   `credit_limit_breached`, check credit_limit (`"Yes"` or `"No"`)
Return the result table in any order.
*/
-- Schema setup.
CREATE TABLE IF NOT EXISTS Users (
    user_id int,
    user_name varchar(20),
    credit int
);
CREATE TABLE IF NOT EXISTS Transactions (
    trans_id int,
    paid_by int,
    paid_to int,
    amount int,
    transacted_on date
);
TRUNCATE TABLE Users;
INSERT INTO Users VALUES ('1', 'Moustafa', '100');
INSERT INTO Users VALUES ('2', 'Jonathan', '200');
INSERT INTO Users VALUES ('3', 'Winston', '10000');
INSERT INTO Users VALUES ('4', 'Luis', '800');
TRUNCATE TABLE Transactions;
INSERT INTO Transactions VALUES ('1', '1', '3', '400', '2020-08-01');
INSERT INTO Transactions VALUES ('2', '3', '2', '500', '2020-08-02');
INSERT INTO Transactions VALUES ('3', '2', '1', '200', '2020-08-03');
-- Solution.
WITH Inflow AS (
    SELECT paid_to,
        SUM(amount) AS plus
    FROM transactions
    GROUP BY paid_to
),
Outflow AS (
    SELECT paid_by,
        SUM(amount) AS
    minus
    FROM transactions
    GROUP BY paid_by
),
Updated AS (
    SELECT u.user_id,
        u.user_name,
        u.credit + COALESCE(i.plus, 0) - COALESCE(o.minus, 0) AS credit
    FROM Users u
        LEFT JOIN Inflow i ON u.user_id = i.paid_to
        LEFT JOIN Outflow o ON u.user_id = o.paid_by
)
SELECT *,
    CASE
        WHEN credit < 0 THEN 'Yes'
        ELSE 'No'
    END AS credit_limit_breached
FROM Updated;