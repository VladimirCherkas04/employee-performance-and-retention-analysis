-- Salary vs Department Average
-- Project: Employee Performance & Retention Analysis

SELECT
    employee_id,
    department,
    job_role,
    salary,
    ROUND(
        AVG(salary) OVER (
            PARTITION BY department
        )::numeric,
        2
    ) AS department_average_salary,
    ROUND(
        (
            salary
            - AVG(salary) OVER (
                PARTITION BY department
            )
        )::numeric,
        2
    ) AS salary_difference
FROM employees
ORDER BY department, salary_difference DESC;