# Sales Analysis Report

## 1. Project Overview
This project analyzes a sales dataset to:
- Calculate **total revenue**
- Identify the **best-selling product**
- Evaluate **regional sales distribution**
- Generate a formatted report for recruiters and reviewers

The analysis demonstrates skills in **data cleaning, aggregation, and reporting** using Python and pandas.

---

## 2. Dataset Summary
- **Rows:** 100 (Jan–Apr 2024)
- **Columns:** Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales
- **Products:** Phone, Laptop, Tablet, Monitor, Headphones
- **Regions:** North, South, East, West

---

## 3. Key Metrics
- **Total Revenue:** ₹12,365,048.00  
- **Best-Selling Product:** **Laptop** (₹3,889,210.00 )  
- **Regional Sales Distribution:**
  - **North:** ₹3983635  
  - **South:** ₹3737852  
  - **East:** ₹2519639
  - **West:** ₹2123922  



---

## 4. Insights
- **Laptops** dominate overall revenue, making them the primary driver of sales.
- **North and South** regions contribute the largest share of revenue.
- **Accessories** (Headphones, Monitors) generate lower revenue but show consistent demand across regions.
- **Tablets** show strong spikes in certain months, suggesting seasonal demand.

---

## 5. Technical Approach
- **Data Loading:** Used pandas `read_csv()` to import dataset.
- **Exploration:** Checked shape, columns, and data types.
- **Cleaning:** Removed missing values and duplicates.
- **Analysis:**  
  - `sum()` for total revenue  
  - `groupby()` for product and regional aggregation  
  - `idxmax()` to identify best-selling product
- **Reporting:** Exported results into Markdown format for readability.

---

## 6. Next Steps
- Focus marketing efforts on **Laptops** in high-performing regions.
- Explore opportunities to **boost accessory sales** (Headphones, Monitors).
- Investigate **seasonal trends** in Tablet sales for targeted promotions.

---

## 7. Validation & Testing
- Verified dataset contains **no missing values**.
- Confirmed **positive revenue totals**.
- Ensured **best-selling product exists** in dataset.

---

## 8. Conclusion
This analysis highlights **Laptops as the revenue leader** and provides actionable insights into regional performance and product demand. The project demonstrates **data analysis, cleaning, and reporting skills** in a recruiter-ready format.

