# Project Revenue & Delivery Performance Audit

## Overview

This self-directed portfolio project answers a practical PM question:

> Which projects are creating commercial value, and which need intervention
> before their budgets are exhausted?

I combined project revenue, budget, status, monthly spend, and KPI data to
measure profitability, compare departments, reconcile spend, and flag active
projects at risk.

## Tools and analysis

- SQLite / SQL
- Filtering, aggregation, grouping, ordering, and joins
- ROI and budget-variance calculations
- `HAVING`-based risk screening
- Python/Pandas risk-report automation

## Dataset

- `campaigns_projects.csv`: project, department, budget, revenue, dates, status
- `monthly_spend_kpis.csv`: monthly spend and KPI performance
- `monthly_spend_kpis_dirty_for_python.csv`: intentionally messy input for
  the Python cleaning workflow
- 20 projects and 32 monthly spend records

## Key findings

- 7 projects generated less revenue than their allocated budget.
- Total revenue was **$1.576M** against **$997K** in allocated budget.
- Product Delivery generated the highest total revenue (**$420K**).
- 6 active projects had consumed more than 80% of their budgets.
- Regional Brand Awareness TV and Warehouse Barcode Rollout were the most
  urgent high-spend, low-return review candidates.

## Analysis flow

1. Identify projects with revenue below budget.
2. Compare department performance and rank ROI.
3. Join project data to monthly spend.
4. Flag active projects above the 80% spend threshold.
5. Produce an automated Excel risk report with Python.

SQL queries: [`02_SQL_Stage/portfolio_queries.sql`](02_SQL_Stage/portfolio_queries.sql)

## Recommended action

Reforecast the high-spend, low-return projects with their owners, reallocate
capacity where appropriate, and monitor spend and KPI performance monthly.

## Deliverables

- SQL analysis: [`02_SQL_Stage/portfolio_queries.sql`](02_SQL_Stage/portfolio_queries.sql)
- Python workflow: [`04_Python_Stage/risk_flagger_starter.py`](04_Python_Stage/risk_flagger_starter.py)
- Excel risk report: [`04_Python_Stage/Automated_Executive_Risk_Report.xlsx`](04_Python_Stage/Automated_Executive_Risk_Report.xlsx)
