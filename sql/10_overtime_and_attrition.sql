-- Overtime & Attrition
-- Project: Employee Performance & Retention Analysis

SELECT
    overtime,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY overtime
ORDER BY attrition_rate DESC;