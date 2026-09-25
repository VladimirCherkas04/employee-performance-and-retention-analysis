-- Attrition by Job Role
-- Project: Employee Performance & Retention Analysis

SELECT
    job_role,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate,
    RANK() OVER (
        ORDER BY
            100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
            / COUNT(*) DESC
    ) AS attrition_rank
FROM employees
GROUP BY job_role
ORDER BY attrition_rank;