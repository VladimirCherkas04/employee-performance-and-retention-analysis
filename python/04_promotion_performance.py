import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data raw" / "employees.csv")


# 1. Promotion rate by performance group

df["performance_group"] = pd.cut(
    df["performance_score"],
    bins=[0, 2.5, 3.5, 4.5, float("inf")],
    labels=["Low", "Medium", "High", "Very High"]
)

performance_promotion = (
    df.groupby("performance_group", observed=True)
    .agg(
        employees=("employee_id", "count"),
        promoted=("promotion", lambda x: (x == "Yes").sum())
    )
    .reset_index()
)

performance_promotion["promotion_rate"] = (
    performance_promotion["promoted"]
    / performance_promotion["employees"]
    * 100
)


print("Promotion by Performance Group")
print("-" * 45)
print(
    performance_promotion
    .round(2)
    .to_string(index=False)
)


# 2. Promotion rate by department

department_promotion = (
    df.groupby("department")
    .agg(
        employees=("employee_id", "count"),
        promoted=("promotion", lambda x: (x == "Yes").sum()),
        average_performance=("performance_score", "mean")
    )
    .reset_index()
)

department_promotion["promotion_rate"] = (
    department_promotion["promoted"]
    / department_promotion["employees"]
    * 100
)

department_promotion = department_promotion.sort_values(
    "promotion_rate",
    ascending=False
)


print("\nPromotion by Department")
print("-" * 45)
print(
    department_promotion
    .round(2)
    .to_string(index=False)
)


# 3. Salary by promotion status

salary_promotion = (
    df.groupby("promotion")
    .agg(
        employees=("employee_id", "count"),
        average_salary=("salary", "mean"),
        average_performance=("performance_score", "mean")
    )
    .reset_index()
)


print("\nSalary and Performance by Promotion Status")
print("-" * 55)
print(
    salary_promotion
    .round(2)
    .to_string(index=False)
)