-- Satisfaction Groups & Attrition
-- Project: Employee Performance & Retention Analysis

SELECT
    CASE
        WHEN job_satisfaction < 2.5 THEN 'Low'
        WHEN job_satisfaction < 3.5 THEN 'Medium'
        WHEN job_satisfaction < 4.5 THEN 'High'
        ELSE 'Very High'
    END AS satisfaction_group,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY satisfaction_group
ORDER BY satisfaction_group;