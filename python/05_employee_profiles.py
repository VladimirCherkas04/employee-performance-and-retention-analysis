import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data raw" / "employees.csv")


# 1. Employee profile by department

department_profile = (
    df.groupby("department")
    .agg(
        employees=("employee_id", "count"),
        average_age_years=("years_at_company", "mean"),
        average_salary=("salary", "mean"),
        average_performance=("performance_score", "mean"),
        average_satisfaction=("job_satisfaction", "mean"),
        average_training_hours=("training_hours", "mean"),
        average_absenteeism=("absenteeism_days", "mean")
    )
    .reset_index()
)

print("Employee Profile by Department")
print("-" * 60)
print(
    department_profile
    .round(2)
    .sort_values("employees", ascending=False)
    .to_string(index=False)
)


# 2. Workforce distribution by age group

age_profile = (
    df.groupby("age_group")
    .agg(
        employees=("employee_id", "count"),
        average_salary=("salary", "mean"),
        average_performance=("performance_score", "mean"),
        average_satisfaction=("job_satisfaction", "mean"),
        attrition_rate=(
            "attrition",
            lambda x: (x == "Yes").mean() * 100
        )
    )
    .reset_index()
)

print("\nWorkforce Profile by Age Group")
print("-" * 60)
print(
    age_profile
    .round(2)
    .to_string(index=False)
)