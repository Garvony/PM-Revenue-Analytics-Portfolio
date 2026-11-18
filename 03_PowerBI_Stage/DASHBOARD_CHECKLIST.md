# Stage 2: Power BI "Money Dashboard" Checklist

## Session 4: Data Model & Raw Charts (45 Mins)
- [ ] 1. Open Power BI Desktop -> `Get Data` -> `Text/CSV`.
- [ ] 2. Load `01_Raw_Data/campaigns_projects.csv` and `01_Raw_Data/monthly_spend_kpis.csv`.
- [ ] 3. Click **Model View** (left sidebar) -> Drag `project_id` from `campaigns_projects` onto `project_id` in `monthly_spend_kpis` to create a 1-to-Many relationship.
- [ ] 4. Switch to **Report View**. Insert a **Clustered Column Chart**:
      - X-axis: `department`
      - Y-axis: `Sum of budget_allocated` and `Sum of revenue_generated`
- [ ] 5. Insert 2 **Card Visuals**:
      - Card 1: Total `revenue_generated`
      - Card 2: Average `kpi_hit`
- [ ] 6. Save file as `03_PowerBI_Stage/Executive_ROI_Dashboard.pbix`. Close laptop.

## Session 5: Interactivity & Bleeding Projects Table (45 Mins)
- [ ] 1. Add a **Slicer** visual -> Drag `department` and `status` into it.
- [ ] 2. Add a **Table** visual showing: `project_name`, `status`, `budget_allocated`, `Sum of amount_spent`, and `Average of kpi_hit`.
- [ ] 3. Sort the table by `Sum of amount_spent` descending to spot budget overruns immediately.

## Session 6: Graphic Design Polish & Portfolio Export (45 Mins)
- [ ] 1. Apply a cohesive dark neutral or clean executive theme.
- [ ] 2. Format revenue bars in **Emerald Green** (`#10B981`) and budget/spend bars in **Slate Grey** (`#64748B`).
- [ ] 3. Add conditional formatting on the Table so `kpi_hit` values below 50 highlight in **Soft Red**.
- [ ] 4. Align all containers with even padding and add a header title: **"Commercial Campaign & Project Delivery ROI Tracker"**.
- [ ] 5. Take 2 high-res screenshots and a 45-second screen recording clicking the Department slicer.
