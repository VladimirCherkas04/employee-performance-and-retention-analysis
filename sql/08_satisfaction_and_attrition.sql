-- Job Satisfaction & Attrition
-- Project: Employee Performance & Retention Analysis

SELECT
    job_satisfaction,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY job_satisfaction
ORDER BY job_satisfaction;