-- Department Ranking by Attrition
-- Project: Employee Performance & Retention Analysis

WITH department_stats AS (
    SELECT
        department,
        COUNT(*) AS employees,
        COUNT(*) FILTER (WHERE attrition = 'Yes') AS employees_left,
        ROUND(
            100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
            / COUNT(*),
            2
        ) AS attrition_rate
    FROM employees
    GROUP BY department
)

SELECT
    department,
    employees,
    employees_left,
    attrition_rate,
    RANK() OVER (
        ORDER BY attrition_rate DESC
    ) AS attrition_rank
FROM department_stats
ORDER BY attrition_rank;