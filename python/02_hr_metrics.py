import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "data raw" / "employees.csv")

# Main HR metrics
total_employees = len(df)

attrition_rate = (
    (df["attrition"] == "Yes").mean() * 100
)

average_salary = df["salary"].mean()

average_performance = df["performance_score"].mean()

average_satisfaction = df["job_satisfaction"].mean()

average_tenure = df["years_at_company"].mean()

average_training_hours = df["training_hours"].mean()

average_absenteeism = df["absenteeism_days"].mean()

print("HR Metrics")
print("-" * 30)

print(f"Total employees: {total_employees}")
print(f"Attrition rate: {attrition_rate:.2f}%")
print(f"Average salary: {average_salary:.2f}")
print(f"Average performance: {average_performance:.2f}")
print(f"Average satisfaction: {average_satisfaction:.2f}")
print(f"Average tenure: {average_tenure:.2f} years")
print(f"Average training hours: {average_training_hours:.2f}")
print(f"Average absenteeism: {average_absenteeism:.2f} days")