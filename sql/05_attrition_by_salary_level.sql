-- Attrition by Salary Level
-- Project: Employee Performance & Retention Analysis

SELECT
    CASE
        WHEN salary < 40000 THEN 'Under 40k'
        WHEN salary < 50000 THEN '40k-49k'
        WHEN salary < 60000 THEN '50k-59k'
        ELSE '60k+'
    END AS salary_level,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY salary_level
ORDER BY attrition_rate DESC;