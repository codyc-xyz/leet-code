Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key (column with unique values) of this table.
item_id is a foreign key (reference column) to the Items table.
buyer_id and seller_id are foreign keys to the Users table.
 

Table: Items

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id is the primary key (column with unique values) of this table.
 

Write a solution to find for each user, the join date and the number of orders they made as a buyer in 2019.

Return the result table in any order.

# Write your MySQL query statement below

WITH UserDetails AS (
    SELECT user_id, join_date
    FROM Users
),

UserOrders AS (
    SELECT order_date, buyer_id, COUNT(buyer_id) AS raw_orders_in_2019 
    FROM Orders
    WHERE SUBSTR(order_date, 1, 4) = "2019"
    GROUP BY buyer_id
)

SELECT user_id AS buyer_id, join_date, COALESCE(raw_orders_in_2019, 0) AS orders_in_2019
FROM UserDetails
LEFT JOIN UserOrders ON UserDetails.user_id = UserOrders.buyer_id;
