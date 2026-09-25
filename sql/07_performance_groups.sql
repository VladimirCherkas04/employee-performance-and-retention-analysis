-- Performance Groups & Promotion
-- Project: Employee Performance & Retention Analysis

SELECT
    CASE
        WHEN performance_score < 2.5 THEN 'Low'
        WHEN performance_score < 3.5 THEN 'Medium'
        WHEN performance_score < 4.5 THEN 'High'
        ELSE 'Very High'
    END AS performance_group,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE promotion = 'Yes') AS promoted,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE promotion = 'Yes')
        / COUNT(*),
        2
    ) AS promotion_rate
FROM employees
GROUP BY performance_group
ORDER BY promotion_rate;