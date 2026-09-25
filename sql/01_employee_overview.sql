-- Employee Overview
-- Project: Employee Performance & Retention Analysis

SELECT
    COUNT(*) AS total_employees,
    COUNT(DISTINCT department) AS departments,
    COUNT(DISTINCT job_role) AS job_roles,
    ROUND(AVG(salary)::numeric, 2) AS average_salary,
    ROUND(AVG(performance_score)::numeric, 2) AS average_performance,
    ROUND(AVG(job_satisfaction)::numeric, 2) AS average_satisfaction,
    ROUND(AVG(years_at_company)::numeric, 2) AS average_years_at_company,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes')
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees;
