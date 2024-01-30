Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

WITH MaxDate AS (
    SELECT product_id, MAX(change_date) AS max_change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT Products.product_id, 
CASE 
    WHEN Products.product_id NOT IN (SELECT MaxDate.product_id FROM MaxDate)
    THEN 10
    ELSE Products.new_price
    END AS price
FROM Products
LEFT JOIN MaxDate ON Products.product_id = MaxDate.product_id 
WHERE Products.change_date = MaxDate.max_change_date OR MaxDate.product_id IS NULL
GROUP BY product_id
ORDER BY product_id, new_price;