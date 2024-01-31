Table: Logs

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

# Write your MySQL query statement below

SELECT L1.num AS ConsecutiveNums
FROM Logs L1
LEFT JOIN Logs L2 ON L2.id = L1.id + 1 AND L1.num = L2.num
LEFT JOIN Logs L3 ON L3.id = L2.id + 1 AND L2.num = L3.num
WHERE L1.num = L3.num
GROUP BY ConsecutiveNums;
