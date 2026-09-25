-- Department, Satisfaction & Attrition
-- Project: Employee Performance & Retention Analysis

WITH satisfaction_groups AS (
    SELECT
        department,
        CASE
            WHEN job_satisfaction < 2.5 THEN 'Low'
            WHEN job_satisfaction < 3.5 THEN 'Medium'
            WHEN job_satisfaction < 4.5 THEN 'High'
            ELSE 'Very High'
        END AS satisfaction_group,
        attrition
    FROM employees
)

SELECT
    department,
    satisfaction_group,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM satisfaction_groups
GROUP BY
    department,
    satisfaction_group
ORDER BY
    department,
    satisfaction_group;