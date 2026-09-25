-- Performance & Promotion Analysis
-- Project: Employee Performance & Retention Analysis

SELECT
    performance_score,
    COUNT(*) AS employees,
    COUNT(*) FILTER (WHERE promotion = 'Yes') AS promoted,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE promotion = 'Yes')
        / COUNT(*),
        2
    ) AS promotion_rate
FROM employees
GROUP BY performance_score
ORDER BY performance_score;