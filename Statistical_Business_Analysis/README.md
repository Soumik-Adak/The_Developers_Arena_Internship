# 📊 Statistical Business Analysis Project

## 📌 Project Overview
This project applies statistical methods to analyze sales performance using transactional datasets.  
The objective is to calculate descriptive statistics, analyze distributions, perform hypothesis testing, correlation analysis, regression modeling, and provide actionable business insights.

---

## 📂 Datasets Used
- **sales_data.csv** – Customer transaction records (Date, Product, Quantity, Price, Region, Total Sales)

---

## 🎯 Goals & Objectives
- Calculate descriptive statistics (mean, median, mode, standard deviation)  
- Analyze data distribution and test for normality  
- Perform correlation analysis between sales drivers  
- Conduct hypothesis tests (t-test, ANOVA, chi-square)  
- Calculate confidence intervals for key metrics  
- Build regression models to quantify relationships  
- Translate findings into actionable recommendations  

---

## 3. Key Metrics
- **Mean Sales:** ₹123,650.48  
- **Median Sales:** ₹97,955.50  
- **Mode Sales:** ₹6,540  
- **Standard Deviation:** ₹100,161.09  
- **95% Confidence Interval for Mean Sales:** (₹103,776.35 , ₹143,524.61)  

---

## 4. Insights
- Sales distribution is **right-skewed**, with large transactions inflating the mean.  
- **Quantity (0.69)** and **Price (0.65)** both strongly correlate with Total Sales.  
- **T-test (East vs West):** Significant difference in mean sales (p = 0.0496).  
- **ANOVA (Regions):** No significant difference across all regions (p = 0.097).  
- **Two-way ANOVA (Region + Product):** No significant effect of region or product (p > 0.13).  
- **Regression Analysis:**  
  - R² = 0.884 → Model explains 88.4% of variance in sales.  
  - Quantity has a stronger impact on sales than price.  

---

## 5. Technical Approach
- **Data Loading:** Used pandas `read_csv()` to import dataset.  
- **Exploration:** Checked shape, columns, and data types.  
- **Cleaning:** Removed missing values and duplicates.  
- **Analysis:**  
  - Descriptive statistics (`mean()`, `median()`, `mode()`, `std()`)  
  - Distribution analysis (histogram, Shapiro-Wilk test)  
  - Correlation (`corr()`, seaborn heatmap)  
  - Hypothesis testing (t-test, ANOVA, two-way ANOVA, chi-square)  
  - Confidence intervals (scipy.stats)  
  - Regression modeling (statsmodels OLS)  
- **Reporting:** Exported results into CSV, TXT, and DOCX formats for recruiter-ready documentation.  

---

## 6. Recommendations
- Focus on **increasing units sold** (quantity) as the strongest driver of revenue.  
- Use **bundling and promotions** to boost sales volume.  
- Apply **regional strategies** where significant differences exist (East vs West).  
- Align inventory planning with **seasonal peaks**.  
- Carefully manage pricing strategies — quantity drives revenue more strongly than price.  

---

## 7. Project Structure
- `statistical_analysis.ipynb` → Notebook with all statistical analysis  
- `sales_data.csv` → Sales dataset  
- `requirements.txt` → Python dependencies  
- `hypothesis_test_result.txt` → Hypothesis test outputs  
- `statistical_report.csv` → Structured summary of results  
- `statistical_report.docx` → Final recruiter-ready document  
- `README.md` → Documentation and screenshots  

---

## 8. Technical Details
- **Libraries Used:** pandas, numpy, matplotlib, seaborn, statsmodels, scipy, plotly  
- **Data Structures:** DataFrames, groupby aggregations, pivot tables  
- **Algorithms:**  
  - Descriptive statistics  
  - Shapiro-Wilk normality test  
  - Pearson correlation  
  - T-test, ANOVA, Chi-square  
  - Confidence intervals  
  - OLS regression  


