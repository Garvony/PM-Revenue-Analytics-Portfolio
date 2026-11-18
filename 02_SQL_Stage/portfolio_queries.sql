-- ============================================================================
-- PROJECT: PROJECT REVENUE & DELIVERY PERFORMANCE AUDIT
-- Purpose: Evaluate project profitability, departmental performance, and
--          budget risk using SQLite.
-- Data sources: campaigns_projects, monthly_spend_kpis
-- Business context: A project-delivery team needs an early view of revenue
-- and spending patterns so it can prioritize intervention and resources.
-- ============================================================================

-- ANALYSIS 1: Identify projects where revenue is below allocated budget.
-- Decision use: Surface projects that may require a profitability review.
SELECT project_id, project_name, department, budget_allocated, revenue_generated
FROM campaigns_projects
WHERE revenue_generated < budget_allocated;



-- ANALYSIS 2: Compare budget and revenue totals by department.
-- Decision use: Give leadership a department-level view of commercial output.
SELECT department,SUM(budget_allocated) AS total_budget, SUM(revenue_generated) AS total_revenue
FROM campaigns_projects
GROUP BY department; 



-- ANALYSIS 3: Rank projects by return on allocated budget.
-- Decision use: Highlight high-performing projects and investigate negative ROI.

SELECT project_name, department,((revenue_generated - budget_allocated) * 100.0 / budget_allocated) AS roi_percentage
FROM campaigns_projects
ORDER BY roi_percentage DESC;

-- ANALYSIS 4: Reconcile project budgets with logged monthly spend.
-- Decision use: Establish the spending baseline for delivery monitoring.

SELECT campaigns_projects.project_name,campaigns_projects.budget_allocated , sum(monthly_spend_kpis.amount_spent) as total_logged_spend
FROM campaigns_projects
INNER JOIN monthly_spend_kpis
ON campaigns_projects.project_id = monthly_spend_kpis.project_id
GROUP BY campaigns_projects.project_name,campaigns_projects.budget_allocated; 

-- ANALYSIS 5: Flag active projects approaching their budget limit.
-- Threshold: Logged spend is greater than 80% of allocated budget.
-- Decision use: Create an early-warning list for project-owner review.
 
SELECT campaigns_projects.project_name,
       campaigns_projects.budget_allocated,
       SUM(monthly_spend_kpis.amount_spent) AS total_logged_spend
from campaigns_projects
INNER JOIN monthly_spend_kpis
    ON campaigns_projects.project_id = monthly_spend_kpis.project_id
WHERE campaigns_projects.status = 'In Progress'
GROUP BY campaigns_projects.project_id,
         campaigns_projects.project_name,
         campaigns_projects.budget_allocated
HAVING SUM(monthly_spend_kpis.amount_spent) >
       (0.8 * campaigns_projects.budget_allocated);
