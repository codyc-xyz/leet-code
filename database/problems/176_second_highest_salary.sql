Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# Write your MySQL query statement below

WITH MaxSalary AS (
    SELECT MAX(salary) AS max_salary FROM Employee
)

SELECT 
    (CASE WHEN COUNT(salary) > 0 THEN MAX(salary) ELSE NULL END) AS SecondHighestSalary 
FROM Employee
LEFT JOIN MaxSalary ON Employee.salary != max_salary
WHERE salary < max_salary
ORDER BY salary DESC
LIMIT 1;