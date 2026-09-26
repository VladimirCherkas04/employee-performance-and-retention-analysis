# Employee Performance & Retention Analysis

## Overview

This portfolio project analyzes employee performance, retention, compensation, job satisfaction, and workforce characteristics using a synthetic HR dataset.

The project demonstrates an end-to-end data analytics workflow using SQL, Python, and Tableau.

> **Important:** The dataset is fully synthetic. It does not contain real employee records, personal data, confidential company information, or official HR statistics. All observed patterns are hypothetical and were created for portfolio and educational purposes.

## Research Questions

The analysis explores:

- Which departments have the highest attrition?
- How does attrition vary across salary levels?
- How is job satisfaction associated with employee attrition?
- Does overtime relate to employee retention?
- How does attrition vary across departments and job roles?
- Is employee performance associated with promotion?
- How do salaries differ across departments and job roles?
- How does workforce structure vary across age groups?
- How does attrition vary across age groups?
- Which job roles have higher synthetic attrition rates?

## Dataset

The dataset contains **5,000 synthetic employee records** and 16 variables.

### Main Variables

| Variable | Description |
|---|---|
| `employee_id` | Synthetic employee identifier |
| `department` | Organizational department |
| `job_role` | Employee's job role |
| `age_group` | Employee age category |
| `gender` | Gender category |
| `education_level` | Education level |
| `years_at_company` | Years employed by the company |
| `salary` | Annual salary |
| `performance_score` | Performance score |
| `job_satisfaction` | Job satisfaction score |
| `overtime` | Whether the employee works overtime |
| `remote_work` | Whether the employee works remotely |
| `promotion` | Whether the employee received a promotion |
| `training_hours` | Annual training hours |
| `absenteeism_days` | Number of absenteeism days |
| `attrition` | Whether the employee left the company |

## Data Note

The dataset is structured as synthetic employee-level records.

The data was generated specifically for analytical and portfolio purposes. Relationships between variables are illustrative and should not be interpreted as evidence of causal relationships in real organizations.

## Analytical Approach

The project follows an end-to-end workflow:

```text
Synthetic HR data
        ↓
PostgreSQL
        ↓
SQL analysis
        ↓
Python analysis
        ↓
Processed datasets
        ↓
Tableau dashboards
        ↓
HR analytics

SQL Analysis

SQL was used for:

- employee-level data validation;
- workforce overview;
- attrition analysis;
- departmental comparisons;
- salary analysis;
- performance and promotion analysis;
- job satisfaction analysis;
- overtime analysis;
- remote work analysis;
- job-role comparisons;
- window functions and ranking;
- multi-dimensional HR analysis.
The project contains 18 analytical SQL queries.

Python Analysis

Python and pandas were used for:

- data loading;
- data quality checks;
- missing-value validation;
- duplicate detection;
- workforce metrics;
- attrition analysis;
- salary analysis;
- satisfaction analysis;
- performance and promotion analysis;
- employee profile analysis;
- preparation of datasets for Tableau.
The Python workflow contains 6 scripts.

Tableau Dashboards

The project contains three dashboards.

HR Overview
Provides a high-level view of the workforce:
- Total Employees
- Average Salary
- Average Performance
- Average Job Satisfaction
- Attrition Rate
- Employees Who Left by Department
- Employees Who Left by Overtime
- Attrition Rate by Salary Level
- Attrition Rate by Job Satisfaction

Attrition Analysis
Focuses on employee retention:
- Attrition Rate by Salary Level
- Attrition Rate by Job Satisfaction
- Attrition Rate by Department

Performance & Workforce
Examines workforce structure and performance:
- Promotion Rate by Performance
- Employees by Age Group
- Average Salary by Age Group
- Attrition Rate by Age Group

Synthetic Findings

The synthetic dataset contains 5,000 employees.
The overall synthetic attrition rate is 12.48%.
The average synthetic salary is approximately 47,462.
The average performance score is 3.31, while the average job satisfaction score is 3.30.
Synthetic attrition varies across departments, salary groups, satisfaction levels, and overtime status.

For example:
- Operations has a synthetic attrition rate of approximately 15.03%.
- Customer Support has a synthetic attrition rate of approximately 10.25%.
- Employees earning under 40k have a synthetic attrition rate of approximately 16.23%.
- Employees earning 60k+ have a synthetic attrition rate of approximately 8.11%.
- Employees working overtime have a synthetic attrition rate of approximately 18.02%.
- Employees not working overtime have a synthetic attrition rate of approximately 10.50%.
- Employees in the low job-satisfaction group have a synthetic attrition rate of approximately 18.47%.
- Employees in the very-high satisfaction group have a synthetic attrition rate of approximately 6.88%.

These figures describe the synthetic dataset only and should not be interpreted as real-world HR benchmarks.

Tools

- PostgreSQL
- DBeaver
- SQL
- Python
- pandas
- Tableau
- GitHub

Skills Demonstrated

- SQL data analysis
- PostgreSQL
- Python and pandas
- Data cleaning and validation
- Exploratory data analysis
- Data transformation
- HR analytics
- Attrition analysis
- Workforce analysis
- Compensation analysis
- Performance analysis
- Data visualization
- Tableau dashboards
- Business analytics

Project Structure

employee-performance-and-retention-analysis/
│
├── README.md
│
├── data/
│   └── employees.csv
│
├── sql/
│   ├── 01_employee_overview.sql
│   ├── 02_attrition_overview.sql
│   ├── ...
│   └── 18_department_satisfaction.sql
│
├── python/
│   ├── 01_data_loading.py
│   ├── 02_hr_metrics.py
│   ├── 03_attrition_analysis.py
│   ├── 04_promotion_performance.py
│   ├── 05_employee_profiles.py
│   └── 06_prepare_tableau_data.py
│
├── tableau/
│   └── employee_performance_retention.twb
│

Limitations
This project is designed for portfolio and educational purposes.
- All data is synthetic.
- The results do not represent real employees or organizations.
- Synthetic correlations should not be interpreted as causal relationships.
- The dataset is illustrative and was created to demonstrate analytical methods and technical skills.
- Attrition patterns should not be treated as real HR benchmarks.

Disclaimer
This project uses fully synthetic data created for portfolio and educational purposes. It does not represent real employees, real organizations, official HR statistics, or confidential company information.
