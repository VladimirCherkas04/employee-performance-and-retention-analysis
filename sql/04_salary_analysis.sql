-- Salary Analysis
-- Project: Employee Performance & Retention Analysis

SELECT
    department,
    COUNT(*) AS employees,
    ROUND(AVG(salary)::numeric, 2) AS average_salary,
    ROUND(AVG(salary) FILTER (WHERE attrition = 'Yes')::numeric, 2) AS average_salary_left,
    ROUND(AVG(salary) FILTER (WHERE attrition = 'No')::numeric, 2) AS average_salary_stayed
FROM employees
GROUP BY department
ORDER BY average_salary DESC;