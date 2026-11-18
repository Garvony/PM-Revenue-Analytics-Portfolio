# ============================================================================
# STAGE 3: AUTOMATED PROJECT RISK FLAGGER (Python + Pandas)
# Goal: Clean messy project logs and output an automated Excel risk report.
# ============================================================================
import pandas as pd
import numpy as np
from pathlib import Path

# --- SESSION 7 (45 Mins): Load & Clean Dirty Data ---
# 1. Load '../01_Raw_Data/campaigns_projects.csv' into df_projects
# 2. Load '../01_Raw_Data/monthly_spend_kpis_dirty_for_python.csv' into df_logs
# 3. Strip leading/trailing whitespace from df_logs['project_id'] using .str.strip()
# 4. Fill missing NaN values in df_logs['amount_spent'] with the median spend
# 5. Print df_logs.info() to verify zero nulls remain.

# Write Session 7 code below:
stage_dir = Path(__file__).resolve().parent
raw_data_dir = stage_dir.parent / "01_Raw_Data"
df_projects = pd.read_csv(raw_data_dir / "campaigns_projects.csv")
df_logs = pd.read_csv(raw_data_dir / "monthly_spend_kpis_dirty_for_python.csv")

df_logs["project_id"] = df_logs["project_id"].str.strip()
df_logs["amount_spent"] = df_logs["amount_spent"].fillna(
    df_logs["amount_spent"].median()
)
df_logs.info()


# --- SESSION 8 (45 Mins): Merge & Flag At-Risk Projects ---
# 1. Group df_logs by 'project_id' to get total 'amount_spent' and average 'kpi_hit'
# 2. Merge with df_projects on 'project_id'
# 3. Create 'burn_rate_pct' = (amount_spent / budget_allocated) * 100
# 4. Use np.where to create a 'risk_flag' column:
#    - If burn_rate_pct > 80 and kpi_hit < 50 -> 'CRITICAL RISK'
#    - Else -> 'ON TRACK'
# 5. Export final dataframe to 'Automated_Executive_Risk_Report.xlsx'

monthly_summary = (
    df_logs.groupby("project_id", as_index=False)
    .agg(amount_spent=("amount_spent", "sum"), kpi_hit=("kpi_hit", "mean"))
)
df_report = df_projects.merge(monthly_summary, on="project_id", how="left")
df_report["burn_rate_pct"] = (
    df_report["amount_spent"] / df_report["budget_allocated"] * 100
).round(2)
df_report["risk_flag"] = np.where(
    (df_report["burn_rate_pct"] > 80) & (df_report["kpi_hit"] < 50),
    "CRITICAL RISK",
    "ON TRACK",
)
df_report["roi_pct"] = (
    (df_report["revenue_generated"] - df_report["budget_allocated"])
    / df_report["budget_allocated"]
    * 100
).round(2)
output_path = stage_dir / "Automated_Executive_Risk_Report.xlsx"
df_report.to_excel(output_path, index=False)
print(f"Exported {len(df_report)} projects to {output_path}")
