/* Consecutive Numbers

Link: https://leetcode.com/problems/consecutive-numbers/

Table: `Logs`

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+

In SQL, id is the primary key for this table.
id is an autoincrement column.


Find all numbers that appear at least three times consecutively.

Return the result table in any order.
*/

SELECT
    DISTINCT(l1.num) AS ConsecutiveNums
FROM
    logs l1
    JOIN logs l2 ON l1.num = l2.num
    AND l2.id = l1.id + 1
    JOIN logs l3 ON l2.num = l3.num
    AND l3.id = l2.id + 1;
