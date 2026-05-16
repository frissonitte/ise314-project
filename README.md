# ISE314 - Data Visualization: E-Commerce Order Management Analysis

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This repository contains my final project for the **ISE314 Data Visualization** course. The project involves procedurally generating a messy, real-world e-commerce dataset using Python, cleaning it via Power Query, and building an interactive, multi-page business intelligence dashboard in Power BI.

### 🔗 Quick Links

- 📓 **[Project Summary & Documentation (Notion)](https://lavish-rhythm-890.notion.site/ISE314-Data-Visualization-Project-Summary-3622c8a2755e806c972dd9d0e31285e0?source=copy_link)**: A complete, step-by-step breakdown of the ETL process, Power Query operations, Data Modeling, and DAX measures.
- 🎥 **[5-Minute Messy Data Generation Presentation (YouTube/Drive Link)](https://youtu.be/Z2Y9onEaVl4)**
- 🎥 **[5-Minute Visualization Part Presentation (YouTube/Drive Link)](https://youtu.be/p993iaYOHTo)**

---

### 📂 Repository Structure

- `create_messy_data.py`: The Python script used to procedurally generate the intentional dirty data (avoids standard Kaggle/Excel datasets).
- `outputs/orders_raw.csv`: The generated fact table containing transaction records, anomalies, and formatting inconsistencies.
- `outputs/products_ref.json`: The dimension table containing product details and stock metrics.
- `artifacts/ISE314_Assignment2_Dashboard.pbix`: The final Power BI project file containing the data model, DAX measures, and visualizations.

---

### 💡 Project Overview

The data simulates a standard e-commerce micro-venture, capturing the lifecycle of digital transactions, physical inventory mapping, and customer feedback. The project addresses common data engineering and visualization challenges, including:

- Handling fragmented data sources (JSON and CSV).
- Parsing conflicting locale formats (e.g., Turkish comma-decimals vs. standard formatting, mixed date structures).
- Tracking operational business flow (Product Category -> Order Status) using advanced visuals like Sankey charts.
- Establishing KPIs to track revenue goals and return rates.

### 📊 Technical Specifications Checklist

| Requirement             | Implementation Detail                                                        |
| :---------------------- | :--------------------------------------------------------------------------- |
| **Data Architecture**   | Star Schema (1:Many Relation) via `product_id`                               |
| **Data Sources**        | Fragmented Hybrid (Local CSV + Local JSON)                                   |
| **Advanced Layout**     | Multi-Page App Architecture with Automated Page Navigation                   |
| **Custom Elements**     | Category-to-Product Hierarchy, Dynamic Time-Based Grouping                   |
| **Advanced Visuals**    | Sankey Flow Chart, Shape Map Geographics, WordCloud, Core KPI Tracker        |
| **Analytical Layer**    | Custom DAX Metrics + Power BI Quick Measure (Running Total)                  |
| **Filtering Framework** | Implemented 3-Level Filter Context (Chart, Page, Report) + Edit Interactions |

### 🚀 How to Reproduce the Data

To generate a fresh batch of dirty data, simply run the Python script. No external libraries are required.

```bash
python create_messy_data.py
```
