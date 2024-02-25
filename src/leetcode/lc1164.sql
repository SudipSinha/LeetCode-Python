/* Product Price at a Given Date

Link: https://leetcode.com/problems/product-price-at-a-given-date/

Table: `Products`

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+

`(product_id, change_date)` is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.


Write a solution to find the prices of all products on `2019-08-16`. Assume the price of all products before any change is `10`.

Return the result table in any order.
*/

-- SET @date_important = CAST('2019-08-16' AS DATE);
WITH
    parameters AS (
        SELECT
            10 AS price_initial,
            CAST('2019-08-16' AS DATE) AS date_important
    ),
    before_20190816 AS (
        SELECT
            product_id,
            new_price AS price,
            RANK() OVER (
                PARTITION BY
                    product_id
                ORDER BY
                    change_date DESC
            ) AS date_rank
        FROM
            products
        WHERE
            change_date <= (
                SELECT
                    date_important
                FROM
                    parameters
            )
    ),
    onafter_20190816 AS (
        SELECT
            product_id
        FROM
            products
        WHERE
            change_date > (
                SELECT
                    date_important
                FROM
                    parameters
            )
    )
SELECT
    product_id,
    price
FROM
    before_20190816
WHERE
    date_rank = 1
UNION
SELECT
    product_id,
    (
        SELECT
            price_initial
        FROM
            parameters
    ) AS price
FROM
    onafter_20190816
WHERE
    product_id NOT IN (
        SELECT
            product_id
        FROM
            before_20190816
    );
