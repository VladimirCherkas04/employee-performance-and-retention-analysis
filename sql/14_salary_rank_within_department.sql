-- Salary Ranking Within Department
-- Project: Employee Performance & Retention Analysis

SELECT
    employee_id,
    department,
    job_role,
    salary,
    RANK() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank_in_department
FROM employees
ORDER BY department, salary_rank_in_department;