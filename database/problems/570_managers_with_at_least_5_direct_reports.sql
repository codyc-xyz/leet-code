Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

# Write your MySQL query statement below

WITH NumReports AS (
    SELECT managerId, COUNT(managerId) AS report_count
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) > 4
)

SELECT name FROM Employee
LEFT JOIN NumReports ON Employee.id = NumReports.managerId
WHERE report_count > 4;

# Write your MySQL query statement below

WITH NumReports AS (
    SELECT managerId, COUNT(managerId) AS report_count
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(managerId) > 4
)

SELECT name FROM Employee
INNER JOIN NumReports ON Employee.id = NumReports.managerId;