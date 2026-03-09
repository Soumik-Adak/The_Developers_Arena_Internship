# 🏡 House Price Prediction – Model Evaluation Report

## 📌 Project Overview
This project builds predictive models to estimate house prices based on property features such as **area, bedrooms, bathrooms, age, location, and property type**.  
The goal is to evaluate multiple machine learning models, compare their performance, and highlight the most impactful features driving property prices.

---

## 📊 Evaluation Metrics

We assessed models using **Mean Absolute Error (MAE)**, **Mean Squared Error (MSE)**, and **R² Score**.

| Model                | MAE (↓)       | MSE (↓)              | R² (↑)   | Notes |
|-----------------------|---------------|----------------------|----------|--------------------------------|
| Linear Regression     | 2,188,736     | 8.45e12              | 0.941    | Strong baseline, interpretable |
| Polynomial Regression | –             | –                    | 1.000    | Perfect fit, likely overfitting |
| Decision Tree         | –             | –                    | 0.936    | Captures non-linear patterns, risk of overfitting |
| Random Forest         | –             | –                    | 0.971    | Best balance of accuracy & generalization |

👉 **Key Insight:** Random Forest achieved the highest generalizable accuracy (R² = 0.971), outperforming Linear Regression and Decision Tree, while Polynomial Regression overfit the dataset.

---

## 📈 Visualizations

### 1. Exploratory Data Analysis
- **Area vs Price Scatter Plot** → Larger properties consistently command higher prices.  
- **Price vs Location Boxplot** → City Center properties are significantly more expensive compared to Suburb and Rural.

### 2. Model Evaluation
- **Predictions vs Actual Scatter Plot** → Predictions closely align with actual values, confirming strong model performance.  
- **Residual Analysis (optional)** → Errors are mostly random, indicating no major bias in predictions.

### 3. Feature Importance (Random Forest)
- **Top Drivers of Price:**
  - **Area** – strongest predictor of price.  
  - **Location** – City Center properties priced highest, Rural lowest.  
  - **Bedrooms & Bathrooms** – add incremental value.  
  - **Age** – older properties depreciate in value.

---

## 📑 Linear Regression Coefficients

| Feature              | Coefficient   | Interpretation |
|----------------------|---------------|----------------|
| Area                 | +7,559        | Larger area increases price significantly |
| Bedrooms             | +1.58M        | Each bedroom adds ~1.58M |
| Bathrooms            | +454K         | Each bathroom adds ~454K |
| Age                  | -82K          | Each year of age reduces price |
| Location_Suburb      | -8.63M        | Suburb properties are cheaper vs City Center |
| Location_Rural       | -16.7M        | Rural properties are much cheaper vs City Center |
| Property_Type_House  | -607K         | Houses slightly cheaper vs Apartments |
| Property_Type_Villa  | +63K          | Villas slightly more expensive vs Apartments |

👉 **Interpretation:** Location and Area dominate pricing, while Age negatively impacts value. Bedrooms and bathrooms add incremental increases.

---

## 🎯 Business Insights

- **Location Premium:** City Center properties command the highest prices, with Rural properties discounted heavily.  
- **Size Matters:** Area is the most consistent driver of price across all models.  
- **Depreciation:** Property age negatively impacts value, reflecting real-world depreciation.  
- **Best Model:** Random Forest provides the most reliable predictions, balancing accuracy and generalization.

---

## ✅ Conclusion

This project demonstrates a full machine learning workflow:
- **EDA → Model Training → Evaluation → Insights.**  
- Random Forest emerges as the best-performing model, with **R² = 0.971**.  
- The analysis confirms that **Area and Location** are the most critical features in determining house prices.  

