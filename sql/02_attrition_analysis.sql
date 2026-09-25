-- Attrition Analysis
-- Project: Employee Performance & Retention Analysis

SELECT
    attrition,
    COUNT(*) AS employees,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS share_percent
FROM employees
GROUP BY attrition
ORDER BY employees DESC;