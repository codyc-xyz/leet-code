Table: Accounts

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.
 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.

WITH CategorizedAccounts AS (
    SELECT account_id,
    CASE 
        WHEN income < 20000 THEN "Low Salary" 
        WHEN income <= 50000 THEN "Average Salary"
        ELSE "High Salary" 
        END AS category
    FROM Accounts
),

CategoryTypes AS (
    SELECT "Low Salary" AS category
    UNION ALL 
    SELECT "Average Salary"
    UNION ALL 
    SELECT "High Salary"
)

SELECT CategoryTypes.category, COALESCE(COUNT(account_id), 0) AS accounts_count 
FROM CategorizedAccounts 
RIGHT JOIN CategoryTypes ON CategorizedAccounts.category = CategoryTypes.category
GROUP BY CategoryTypes.category; 