# Technical Documentation
## Business Intelligence & Predictive Analytics Suite

**Version:** 1.0  
**Date:** April 2026  
**Classification:** Internal Technical Reference

---

## 1. System Architecture

### 1.1 Data Pipeline

```
[Raw CSV Files]
     │
     ▼
[Data Ingestion]         pandas.read_csv with schema validation
     │
     ▼
[Data Quality Check]     Null detection, duplicate removal, type coercion
     │
     ▼
[Feature Engineering]    Label encoding for categoricals, StandardScaler for numerics
     │
     ▼
[Train/Test Split]       80/20 stratified split (churn) | 80/20 random split (house)
     │
     ▼
[Model Training]         RandomForestClassifier | RandomForestRegressor
     │
     ▼
[Evaluation]             Hold-out metrics + 5-fold cross-validation
     │
     ▼
[Serialization]          joblib.dump → .pkl files in deployment/
     │
     ▼
[REST API]               Flask endpoints serving real-time predictions
```

---

## 2. Algorithms & Data Structures

### 2.1 Random Forest Classifier (Churn)

**Algorithm:** Ensemble of 100 decision trees trained via bootstrap aggregation (bagging).

**Key Hyperparameters:**
| Parameter | Value | Rationale |
|---|---|---|
| n_estimators | 100 | Sufficient for dataset size; diminishing returns beyond |
| max_features | "sqrt" (default) | Reduces correlation between trees |
| random_state | 42 | Reproducibility |
| class_weight | None | Dataset is mildly imbalanced (10.6% churn); acceptable |

**Feature Preprocessing:**
- Categorical features (Contract, PaymentMethod, PaperlessBilling): `LabelEncoder` — ordinal encoding adequate for tree-based models
- Numeric features: `StandardScaler` — applied before training; scaler fitted only on training data to prevent data leakage

**Why Random Forest over Logistic Regression?**
- Non-linear interactions between Tenure and Contract type
- Robust to outliers in TotalCharges
- Built-in feature importance without regularization tuning
- ROC-AUC gain: RF (0.9939) vs LR (estimated ~0.85 on this dataset)

### 2.2 Random Forest Regressor (House Price)

**Algorithm:** Same bagging principle, predicting continuous price values via averaging leaf-node outputs.

**Key Hyperparameters:** Identical to classifier above (`n_estimators=100`, `random_state=42`).

**Feature Encoding:**
- Location (Rural/Suburb/Urban): LabelEncoder (ordinal)
- Property_Type (Apartment/House/Villa): LabelEncoder
- No scaling required — tree models are scale-invariant for regression

**Why not Linear Regression?**
- Non-linear price-area relationship (urban premium, property type interaction)
- R² improvement: RF (0.9725) vs expected LR (~0.75-0.80)

### 2.3 Sales Analytics

**Approach:** Descriptive statistics via pandas groupby aggregations:
```python
product_revenue = sales.groupby('Product')['Total_Sales'].sum()
region_revenue  = sales.groupby('Region')['Total_Sales'].sum()
monthly_revenue = sales.groupby('Month')['Total_Sales'].sum()
```

No predictive model required — the dataset (100 records, 1 month of data) is insufficient for time-series forecasting. Analytics focus on cross-sectional insights.

---

## 3. Data Structures

### 3.1 Input Schemas

**Customer Churn Input:**
```json
{
  "Tenure"           : 24,
  "MonthlyCharges"   : 80,
  "TotalCharges"     : 1920,
  "Contract"         : "One year",
  "PaymentMethod"    : "Credit card",
  "PaperlessBilling" : "Yes",
  "SeniorCitizen"    : 0
}
```

**House Price Input:**
```json
{
  "Area"          : 2000,
  "Bedrooms"      : 3,
  "Bathrooms"     : 2,
  "Age"           : 5,
  "Location"      : "Urban",
  "Property_Type" : "Apartment"
}
```

### 3.2 Output Schemas

**Churn Response:**
```json
{
  "churn_prediction"  : 0,
  "churn_probability" : 0.12,
  "risk_level"        : "Low",
  "recommendation"    : "Customer appears stable"
}
```

**House Price Response:**
```json
{
  "estimated_price"   : 24500000,
  "price_formatted"   : "₹2,45,00,000",
  "price_range_low"   : "₹2,20,50,000",
  "price_range_high"  : "₹2,69,50,000",
  "confidence"        : "±10%"
}
```

---

## 4. Feature Engineering Details

### 4.1 Churn Features

| Feature | Type | Engineering | Importance |
|---|---|---|---|
| TotalCharges | Numeric | None (scaled) | 0.2341 |
| Tenure | Numeric | None (scaled) | 0.2198 |
| MonthlyCharges | Numeric | None (scaled) | 0.2087 |
| Contract_enc | Ordinal | LabelEncoder | 0.1432 |
| PaymentMethod_enc | Ordinal | LabelEncoder | 0.0812 |
| SeniorCitizen | Binary | Native | 0.0721 |
| PaperlessBilling_enc | Binary | LabelEncoder | 0.0409 |

### 4.2 House Price Features

| Feature | Type | Engineering | Importance |
|---|---|---|---|
| Area | Numeric | None | ~0.55 |
| Location_enc | Ordinal | LabelEncoder | ~0.18 |
| Age | Numeric | None | ~0.12 |
| Bedrooms | Numeric | None | ~0.08 |
| PropertyType_enc | Ordinal | LabelEncoder | ~0.05 |
| Bathrooms | Numeric | None | ~0.02 |

---

## 5. Model Evaluation Methodology

### 5.1 Churn Model Evaluation

**Primary metric:** ROC-AUC — appropriate for imbalanced binary classification (10.6% positive rate).

**Secondary metrics:**
- Precision: Fraction of predicted churners who actually churned (minimise false positives → wasted retention spend)
- Recall: Fraction of actual churners caught (minimise false negatives → missed revenue)
- F1-Score: Harmonic mean — used for class-level comparison

**Cross-Validation:** Stratified 5-fold CV on full dataset ensures churn class proportion is preserved in each fold. Mean ROC-AUC: 0.9946 ± 0.0022 — low variance indicates stable generalisation.

### 5.2 House Price Model Evaluation

**Primary metric:** R² (coefficient of determination) — proportion of price variance explained by the model.

**Secondary metrics:**
- MAE (₹15.1L): Average absolute prediction error — interpretable in domain currency
- RMSE (₹19.8L): Penalises large errors more heavily; useful for risk assessment
- MAE as % of mean price: 6.1% — well below the 15% target threshold

---

## 6. API Design

### 6.1 Error Handling
- `400 Bad Request`: Missing required field (KeyError caught, field name returned)
- `500 Internal Server Error`: Unexpected model/transform failure (exception message returned)
- All errors return JSON with `{"error": "..."}` structure

### 6.2 Encoding Maps (Server-Side)
```python
CONTRACT_MAP      = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
PAYMENT_MAP       = {'Bank transfer': 0, 'Credit card': 1,
                     'Electronic check': 2, 'Mailed check': 3}
LOCATION_MAP      = {'Rural': 0, 'Suburb': 1, 'Urban': 2}
PROPERTY_TYPE_MAP = {'Apartment': 0, 'House': 1, 'Villa': 2}
```

Encoding is applied server-side so clients send human-readable strings.

---

## 7. Testing Evidence

### 7.1 Churn API Test Cases

| Scenario | Input | Expected Risk | Result |
|---|---|---|---|
| Short-tenure, M2M | Tenure=2, Contract=Month-to-month | High | ✅ High |
| Long-tenure, 2-year | Tenure=60, Contract=Two year | Low | ✅ Low |
| Missing field | No Tenure field | 400 error | ✅ Error returned |
| Senior, electronic check | SeniorCitizen=1, PaymentMethod=Electronic check | Medium-High | ✅ Medium |

### 7.2 House Price API Test Cases

| Scenario | Input | Expected Range | Result |
|---|---|---|---|
| Small rural property | Area=600, Location=Rural | < ₹1 Cr | ✅ ~₹72L |
| Large urban villa | Area=4500, Location=Urban, Type=Villa | > ₹4 Cr | ✅ ~₹4.8 Cr |
| Missing field | No Area field | 400 error | ✅ Error returned |

### 7.3 Data Quality Results

| Dataset | Rows | Missing Values | Duplicates | Status |
|---|---|---|---|---|
| customer_churn.csv | 500 | 0 | 0 | ✅ Clean |
| house_prices.csv | 300 | 0 | 0 | ✅ Clean |
| sales_data.csv | 100 | 0 | 0 | ✅ Clean |

---

## 8. Known Limitations & Future Work

| Limitation | Impact | Proposed Solution |
|---|---|---|
| Churn class imbalance (10.6%) | Lower F1 on churn class (0.78) | SMOTE oversampling or class_weight='balanced' |
| House model trained on Indian market only | Cannot generalise globally | Add location metadata; retrain per market |
| Sales data is 1 month | Cannot forecast seasonality | Collect 12+ months; add ARIMA/Prophet |
| No authentication on API | Production security risk | Add JWT token middleware |
| No model drift monitoring | Silent accuracy degradation | Implement Evidently AI monitoring |
