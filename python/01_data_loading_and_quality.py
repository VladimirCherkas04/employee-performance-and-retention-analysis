import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data raw" / "employees.csv"
df = pd.read_csv(file_path)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nUnique values:")
print(df.nunique())