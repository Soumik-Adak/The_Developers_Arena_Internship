# E-commerce Sales Analysis

Welcome to the **E-commerce Sales Analysis** project!  


---

## 📌 Project Overview
This report analyzes an e-commerce sales dataset (Jan–Apr 2024) to:
- Calculate total revenue
- Identify the best-selling product
- Evaluate regional sales distribution
- Visualize sales trends with multiple chart types

---

## 🎯 Goals & Objectives
- **Data Cleaning:** Handle missing values and duplicates  
- **Date Conversion:** Convert string dates into datetime for daily/monthly analysis  
- **Metric Calculation:** Compute revenue, product sales, and regional distribution  
- **Visualization:** Create bar, pie, and line charts using `matplotlib`  
- **Reporting:** Export results into Markdown with charts and insights  
- **Documentation & Testing:** Provide README, test cases, and screenshots  


---

## 🔧 Setup Instructions (VS Code)
1. **Install Python** (3.8 or higher).
2. **Create folder**:
3. **Open in VS Code**: File → Open Folder → select `ecommerce_sales_analysis`.
4. **Add files**:
- `analysis.ipynb`
- `README.md`
- `requirements.txt`
- `visualizations/` (add your PNG screenshots here)
- `data/sales_data.csv` (add dataset here)
- `report/analysis_report.md` (add analysis report here)

---

## 🐍 Source Code

View the main program file:  
👉 [analysis.ipynb](analysis.ipynb)


---

## 📸 visualizations

Example program runs are saved in the **visualizations/** folder:

- [Screenshot1.png](Screenshot1.png)  
  

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

## 7. Validation & Testing
- Verified dataset contains **no missing values**.
- Confirmed **positive revenue totals**.
- Ensured **best-selling product exists** in dataset.

