# ============================================================================
# INDEPENDENT PROJECT: AUTOMATED PROJECT RISK FLAGGER
# Tools: Python, Pandas, NumPy
#
# Project brief
# Build a repeatable reporting workflow that turns inconsistent project
# activity logs into an executive-ready risk report. The finished analysis
# should help a project manager identify projects that are spending heavily
# while failing to meet their KPI targets.
#
# Your objectives
# - Inspect and clean the source data before using it.
# - Combine project budgets, spend, and KPI performance into one report.
# - Define a transparent rule for identifying critical project risk.
# - Export a reusable Excel deliverable and verify the resulting data.
#
# Expected deliverable
# Create `Automated_Executive_Risk_Report.xlsx` in this folder. It should
# contain one row per project, the calculated burn rate and ROI, and a
# `risk_flag` that distinguishes critical risk from projects that are on track.
#
# Success criteria
# - Project IDs match correctly after whitespace is removed.
# - Missing spend values are handled using a documented, defensible value.
# - Spend and KPI metrics are summarized at project level before the merge.
# - Risk flags follow the stated burn-rate and KPI thresholds.
# - The exported workbook can be opened and traced back to the source files.
# ============================================================================
import pandas as pd
import numpy as np
from pathlib import Path

# --- Phase 1: Inspect and clean the source data ---
# Load the project master data and the monthly activity log from
# `01_Raw_Data`. Normalize project IDs, handle missing spend values, and
# inspect the cleaned log so you can confirm the inputs are analysis-ready.

stage_dir = Path(__file__).resolve().parent
raw_data_dir = stage_dir.parent / "01_Raw_Data"
df_projects = pd.read_csv(raw_data_dir / "campaigns_projects.csv")
df_logs = pd.read_csv(raw_data_dir / "monthly_spend_kpis_dirty_for_python.csv")

df_logs["project_id"] = df_logs["project_id"].str.strip()
df_logs["amount_spent"] = df_logs["amount_spent"].fillna(
    df_logs["amount_spent"].median()
)
df_logs.info()


# --- Phase 2: Build the risk model and executive report ---
# Summarize each project's total spend and average KPI performance, then
# merge those metrics with the project master data.
#
# Risk rule:
# - `burn_rate_pct > 80` and `kpi_hit < 50` -> `CRITICAL RISK`
# - Otherwise -> `ON TRACK`
#
# Add burn rate and ROI calculations, export the final report, and review the
# exported row count and file path as a final quality check.

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
