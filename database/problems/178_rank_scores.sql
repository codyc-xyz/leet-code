Table: Scores

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.

# Write your MySQL query statement below

SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores;


SELECT S1.score, COUNT(DISTINCT S2.score) AS 'rank'
FROM Scores S1, Scores S2
WHERE S1.score <= S2.score
GROUP BY S1.id
ORDER BY score DESC;