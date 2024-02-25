/* Count Salary Categories

Link: https://leetcode.com/problems/count-salary-categories/

Table: `Accounts`

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+

`account_id` is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.


Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

`"Low Salary"`: All the salaries strictly less than `20000`.
`"Average Salary"`: All the salaries in the inclusive range `[20000, 50000]`.
`"High Salary"`: All the salaries strictly greater than `50000`.
The result table must contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in any order.
*/
-- Approach 1. Does not run for some reason.
CREATE TEMPORARY TABLE IF NOT EXISTS category_defaults (category varchar, default_count int);

TRUNCATE TABLE category_defaults;

INSERT INTO
    category_defaults
VALUES
    ('Low Salary', 0);

INSERT INTO
    category_defaults
VALUES
    ('Average Salary', 0);

INSERT INTO
    category_defaults
VALUES
    ('High Salary', 0);

WITH
    parameters AS (
        SELECT
            20000 AS low_max,
            50000 AS high_min
    ),
    categories AS (
        SELECT
            CASE
                WHEN income < (
                    SELECT
                        low_max
                    FROM
                        parameters
                ) THEN 'Low Salary'
                WHEN income > (
                    SELECT
                        high_min
                    FROM
                        parameters
                ) THEN 'High Salary'
                ELSE 'Average Salary'
            END AS category
    ),
    category_counts AS (
        SELECT
            category,
            count(*) AS accounts_count
        FROM
            categories
        GROUP BY
            category
    )
SELECT
    category_defaults.category,
    MAX(default_count, accounts_count)
FROM
    category_defaults
    LEFT JOIN category_counts ON category_defaults.category = category_counts.category;

-- Approach 2: Unpivot
WITH
    parameters AS (
        SELECT
            20000 AS low_max,
            50000 AS high_min
    ),
    categoried AS (
        SELECT
            *,
            CASE
                WHEN income < (
                    SELECT
                        low_max
                    FROM
                        parameters
                ) THEN 1
                ELSE 0
            END AS 'L',
            CASE
                WHEN income BETWEEN (
                    SELECT
                        low_max
                    FROM
                        parameters
                ) AND (
                    SELECT
                        high_min
                    FROM
                        parameters
                )  THEN 1
                ELSE 0
            END AS 'A',
            CASE
                WHEN income > (
                    SELECT
                        high_min
                    FROM
                        parameters
                ) THEN 1
                ELSE 0
            END AS 'H'
        FROM
            accounts
    )
-- Unpivot
SELECT
    'Low Salary' AS category,
    sum(L) AS accounts_count
FROM
    categoried
UNION
SELECT
    'Average Salary' AS category,
    sum(A) AS accounts_count
FROM
    categoried
UNION
SELECT
    'High Salary' AS category,
    sum(H) AS accounts_count
FROM
    categoried;
