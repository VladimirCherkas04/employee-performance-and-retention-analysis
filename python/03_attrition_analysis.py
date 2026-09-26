import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data raw" / "employees.csv")


# 1. Attrition by department

department_attrition = (
    df.groupby("department")
    .agg(
        employees=("employee_id", "count"),
        employees_left=("attrition", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

department_attrition["attrition_rate"] = (
    department_attrition["employees_left"]
    / department_attrition["employees"]
    * 100
)

department_attrition = department_attrition.sort_values(
    "attrition_rate",
    ascending=False
)


print("Attrition by Department")
print("-" * 40)
print(department_attrition.round(2).to_string(index=False))


# 2. Attrition by salary level

df["salary_level"] = pd.cut(
    df["salary"],
    bins=[0, 40000, 50000, 60000, float("inf")],
    labels=["Under 40k", "40k-49k", "50k-59k", "60k+"]
)

salary_attrition = (
    df.groupby("salary_level", observed=True)
    .agg(
        employees=("employee_id", "count"),
        employees_left=("attrition", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

salary_attrition["attrition_rate"] = (
    salary_attrition["employees_left"]
    / salary_attrition["employees"]
    * 100
)


print("\nAttrition by Salary Level")
print("-" * 40)
print(salary_attrition.round(2).to_string(index=False))


# 3. Attrition by job satisfaction

df["satisfaction_group"] = pd.cut(
    df["job_satisfaction"],
    bins=[0, 2.5, 3.5, 4.5, float("inf")],
    labels=["Low", "Medium", "High", "Very High"]
)

satisfaction_attrition = (
    df.groupby("satisfaction_group", observed=True)
    .agg(
        employees=("employee_id", "count"),
        employees_left=("attrition", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

satisfaction_attrition["attrition_rate"] = (
    satisfaction_attrition["employees_left"]
    / satisfaction_attrition["employees"]
    * 100
)


print("\nAttrition by Job Satisfaction")
print("-" * 40)
print(satisfaction_attrition.round(2).to_string(index=False))


# 4. Attrition by overtime

overtime_attrition = (
    df.groupby("overtime")
    .agg(
        employees=("employee_id", "count"),
        employees_left=("attrition", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

overtime_attrition["attrition_rate"] = (
    overtime_attrition["employees_left"]
    / overtime_attrition["employees"]
    * 100
)

overtime_attrition = overtime_attrition.sort_values(
    "attrition_rate",
    ascending=False
)


print("\nAttrition by Overtime")
print("-" * 40)
print(overtime_attrition.round(2).to_string(index=False))