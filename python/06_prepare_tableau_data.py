import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data raw" / "employees.csv")

OUTPUT_DIR = BASE_DIR / "data raw" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


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

department_attrition.to_csv(
    OUTPUT_DIR / "attrition_by_department.csv",
    index=False,
    sep=";"
)


# 2. Attrition by salary

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

salary_attrition.to_csv(
    OUTPUT_DIR / "attrition_by_salary.csv",
    index=False,
    sep=";"
)


# 3. Attrition by satisfaction

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

satisfaction_attrition.to_csv(
    OUTPUT_DIR / "attrition_by_satisfaction.csv",
    index=False,
    sep=";"
)


# 4. Promotion by performance

df["performance_group"] = pd.cut(
    df["performance_score"],
    bins=[0, 2.5, 3.5, 4.5, float("inf")],
    labels=["Low", "Medium", "High", "Very High"]
)

promotion_performance = (
    df.groupby("performance_group", observed=True)
    .agg(
        employees=("employee_id", "count"),
        promoted=("promotion", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

promotion_performance["promotion_rate"] = (
    promotion_performance["promoted"]
    / promotion_performance["employees"]
    * 100
)

promotion_performance.to_csv(
    OUTPUT_DIR / "promotion_by_performance.csv",
    index=False,
    sep=";"
)


# 5. Workforce by age

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

age_profile.to_csv(
    OUTPUT_DIR / "workforce_by_age.csv",
    index=False,
    sep=";"
)


print("Tableau datasets prepared successfully.")
print(f"Output directory: {OUTPUT_DIR}")

print("\nFiles created:")
for file in OUTPUT_DIR.glob("*.csv"):
    print("-", file.name)