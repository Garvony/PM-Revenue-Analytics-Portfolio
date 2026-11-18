# Project Revenue & Delivery Performance Audit

## Portfolio case study

I independently built this analysis to answer a practical project-management
question:

> Which projects are creating commercial value, and which active projects need
> intervention before their budgets are exhausted?

The project combines project-level revenue and budget data with monthly logged
spend. I used SQLite-style SQL analysis to identify profitability gaps, compare
departments, rank return on budget, reconcile spend, and create an early-warning
list for active projects.

## Tools and skills

- SQLite / SQL
- Filtering, aggregation, grouping, ordering
- ROI and budget-variance calculations
- INNER JOINs across project and monthly-spend tables
- `HAVING`-based risk screening
- Business-focused interpretation and executive communication

## Dataset

- `campaigns_projects.csv`: project, department, budget, revenue, start date,
  and status
- `monthly_spend_kpis.csv`: project-month spend and KPI performance
- 20 projects and 32 monthly spend records

## Key findings

- **7 projects** generated less revenue than their allocated budget.
- **$1.576M** in revenue was generated against **$997K** in allocated budget.
- **Product Delivery** produced the highest total revenue at **$420K**.
- **6 active projects** had logged spend above **80%** of their budget:
  Influencer Affiliate Push, Regional Brand Awareness TV, VIP Client Fast-Track
  Portal, Warehouse Barcode Rollout, AI Helpdesk Deflection Pilot, and
  Automated Billing Recovery.
- The most urgent review candidates combine high spend exposure with weak
  commercial performance, especially Regional Brand Awareness TV and Warehouse
  Barcode Rollout.

## Analysis flow

1. Find projects where revenue is below allocated budget.
2. Compare budget and revenue by department.
3. Rank projects by return on allocated budget.
4. Join project budgets to monthly logged spend.
5. Flag active projects where logged spend exceeds 80% of budget.

The source queries are available in
[`02_SQL_Stage/portfolio_queries.sql`](../02_SQL_Stage/portfolio_queries.sql).

## Recommended actions

1. Review the six budget-risk projects with their project owners.
2. Reforecast projects with high spend but negative or weak ROI.
3. Reallocate capacity toward high-ROI work where delivery status allows.
4. Track spend and KPI performance monthly rather than waiting for project
   closeout.

## Visual evidence

### Executive overview

![Executive overview](sql_analysis_overview.png)

### Department performance

![Department performance](department_performance.png)

### Budget-risk alerts

![Budget-risk alerts](budget_risk_alerts.png)

## How to present this project

Use the following 60-second walkthrough:

1. **Context:** "I wanted to understand where project budgets were producing
   revenue and where delivery teams needed an early warning."
2. **Method:** "I joined project-level commercial data to monthly spend and
   used SQL aggregation, ROI calculations, and an 80% budget threshold."
3. **Insight:** "Seven projects were below budget on revenue, while six active
   projects had already consumed more than 80% of their allocated budget."
4. **Action:** "I would prioritize a reforecast and owner review for the
   high-spend, low-return projects, then monitor them monthly."

This framing demonstrates business judgment, not just SQL syntax.

