# 📊 Customer Sales Analysis

## Overview
This project analyzes customer purchasing behavior and churn patterns using **sales data** and **customer churn records**.  
The goal is to identify valuable customers, product performance, regional sales distribution, seasonal trends, and churn risks.  
The project produces a recruiter‑ready dashboard and a professional analysis report.

---

## Features
- 📈 **Executive Summary Report** with revenue, customer count, average order value, and top customer  
- 👥 **Customer Insights**: Identify most valuable customers and churn risks  
- 🛒 **Product Analysis**: Best-selling products and cross-selling opportunities  
- 🌍 **Regional Performance**: Sales distribution across regions  
- 📅 **Seasonal Trends**: Monthly and quarterly sales patterns  
- 🔄 **Retention Strategies**: Recommendations to reduce churn  
- 🖥️ **Visual Dashboard**: Interactive charts and tables (via Streamlit)  
- 📄 **PDF Report**: Automatically generated analysis report with insights  

---

## Setup Instructions
1. **Install Python** (3.8 or higher).
3. **Run Jupyter Notebook** 
4. **Add files**:
- `customer_analysis.ipynb`
- `README.md`
- `requirements.txt`
- `visualizations/` (add your PNG screenshots here)
- `data/sales_data.csv` (add dataset here)
- `data/customer_churn.csv` (add dataset here)
- `report/analysis_report.md` (add analysis report here)
---

## 🐍 Source Code

View the main program file:  
👉 [customer_analysis.ipynb](customer_analysis.ipynb)


---

## 📸 visualizations

Example program runs are saved in the **visualizations/** folder:

- [Product Sales Bar Chart](visualizations/bar_chart.png)
- [Regional Sales Pie Chart](visualizations/pie_chart.png)
- [Sales Trend Over Time](visualizations/line_chart.png) 
  

---


## Key Metrics
- **Total Revenue:** ₹12,365,048.00  
- **Total Customers:** 500 
- **Average Order Value:** $123,650
- **Top Customer:** C00016 - $373,932 
   


---


## Insights

- **Top Customers**: A small group of customers (e.g., C00016, C00007, C00083) generate disproportionately high revenue, highlighting the importance of customer loyalty and retention programs.  
- **Product Performance**:  
  - **Laptops** dominate overall revenue, especially in the North and South regions.  
  - **Phones** also contribute significantly, particularly in the South region.  
  - **Accessories** (Headphones, Monitors) generate lower revenue but show consistent demand across regions.  
  - **Tablets** exhibit strong seasonal spikes, especially in the East and North regions.  
- **Regional Sales**:  
  - The **North (32.2%)** and **South (30.2%)** regions contribute the largest share of total sales.  
  - The **East (20.4%)** region shows moderate performance, while the **West (17.2%)** lags behind.  
- **Seasonal Trends**: Monthly sales fluctuate significantly, with peaks around Q1 and Q3, followed by sharp declines. This indicates strong seasonal demand cycles that require proactive inventory planning.  
- **Customer Concentration**: Revenue is heavily concentrated among the top 10 customers, suggesting that churn among these accounts would have a major impact on overall performance.    

