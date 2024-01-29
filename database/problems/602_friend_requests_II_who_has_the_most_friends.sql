Table: RequestAccepted

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

# Write your MySQL query statement below

WITH MaxRequests AS (
    SELECT requester_id, COUNT(requester_id) AS num_requests
    FROM RequestAccepted
    GROUP BY requester_id
),

MaxAccepts AS (
    SELECT accepter_id, COUNT(accepter_id) AS num_accepts
    FROM RequestAccepted
    GROUP BY accepter_id
)

SELECT COALESCE(MaxRequests.requester_id, MaxAccepts.accepter_id) AS id, 
(COALESCE(num_requests, 0) + COALESCE(num_accepts, 0)) AS num
FROM MaxRequests
LEFT JOIN MaxAccepts ON MaxRequests.requester_id = MaxAccepts.accepter_id

UNION

SELECT COALESCE(MaxRequests.requester_id, MaxAccepts.accepter_id) AS id, 
(COALESCE(num_requests, 0) + COALESCE(num_accepts, 0)) AS num
FROM MaxRequests
RIGHT JOIN MaxAccepts ON MaxRequests.requester_id = MaxAccepts.accepter_id

GROUP BY MaxRequests.requester_id, MaxAccepts.accepter_id
ORDER BY num DESC
LIMIT 1;