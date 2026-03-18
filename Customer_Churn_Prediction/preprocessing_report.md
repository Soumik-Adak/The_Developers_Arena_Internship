# 🔧 Preprocessing Report — Customer Churn Prediction

## Dataset Overview

| Property | Value |
|---|---|
| Rows | 500 |
| Columns (raw) | 9 |
| Columns (after engineering) | 19 |
| Missing Values | 0 |
| Class Distribution | 89.4% Retained / 10.6% Churned |

---

## Step 1 — Data Exploration (Day 1)

**Objective:** Understand the structure, distributions, and quality of the raw data.

**Actions Taken:**
- Loaded CSV and inspected shape, dtypes, and null counts
- Computed descriptive statistics for all numeric columns
- Analysed target variable (`Churn`) distribution: **447 retained vs 53 churned** — moderately imbalanced (~10.6% churn rate)
- Inspected unique values for categorical columns

**Key Findings:**
- `Tenure` ranges 1–71 months (mean ~36.5)
- `MonthlyCharges` ranges 20–199 (mean ~113.6)
- `TotalCharges` ranges 159–7992 (mean ~4238)
- No missing values — data is clean
- `Contract` has natural ordinal order (Month-to-month < One year < Two year)

---

## Step 2 — Categorical Encoding (Day 2)

Three encoding strategies were applied based on the nature of each variable.

### 2a. Label Encoding — `PaperlessBilling`
- **Rationale:** Binary Yes/No variable maps naturally to 0/1 without introducing spurious ordering between three or more classes
- **Result:** `PaperlessBilling_LE` (No → 0, Yes → 1)
- **Library:** `sklearn.preprocessing.LabelEncoder`

### 2b. Ordinal Encoding — `Contract`
- **Rationale:** Contract length has a natural, meaningful order: Month-to-month (shortest commitment) → One year → Two year (longest). Ordinal encoding preserves this relationship, which tree-based models can exploit
- **Result:** `Contract_OE` (Month-to-month → 0, One year → 1, Two year → 2)
- **Library:** `sklearn.preprocessing.OrdinalEncoder`

### 2c. One-Hot Encoding — `PaymentMethod`
- **Rationale:** Payment method is purely nominal — no ordering exists between Credit Card, Electronic Check, and Bank Transfer. One-hot prevents the model from inferring false ordinal relationships
- **Result:** `PM_Credit_Card`, `PM_Electronic_Check` (drop-first to avoid multicollinearity; Bank Transfer is the implicit baseline)
- **Library:** `sklearn.preprocessing.OneHotEncoder(drop='first')`

---

## Step 3 — Feature Scaling (Day 3)

Two scalers were applied to all numeric features and compared.

### 3a. Standard Scaler (Z-score normalisation)
- **Formula:** `(x - mean) / std`
- **Result:** Mean ≈ 0, Std ≈ 1 for each feature
- **Best for:** Linear models (Logistic Regression), distance-based models (KNN, SVM), features with approximate Gaussian distribution
- **Applied to:** `Tenure`, `MonthlyCharges`, `TotalCharges`, `CLV`, `ChargePerMonth`, `MonthlyTotalRatio`

### 3b. Min-Max Scaler (normalisation)
- **Formula:** `(x - min) / (max - min)`
- **Result:** All values in [0, 1]
- **Best for:** Neural networks, algorithms sensitive to feature magnitudes, bounded outputs
- **Applied to:** Same numeric columns

**Comparison:**  
Standard scaling is used in the final pipeline since the dataset includes skewed distributions (`TotalCharges`, `CLV`) where StandardScaler is more robust to extreme values than MinMax.

---

## Step 4 — Outlier Detection & Handling (Day 4)

Two methods were used to detect outliers across key numeric columns.

| Column | IQR Outliers | Z-Score Outliers (|z|>3) | Action |
|---|---|---|---|
| MonthlyCharges | 0 | 0 | No action needed |
| TotalCharges | 0 | 0 | No action needed |
| Tenure | 0 | 0 | No action needed |

**Methods:**
- **IQR Method:** Flags values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR
- **Z-Score Method:** Flags values with |z| > 3 (more than 3 standard deviations from mean)

**Conclusion:** This dataset is clean with no detectable outliers in key numeric features, suggesting the data has already been curated or capped at reasonable business limits.

---

## Step 5 — Feature Engineering (Day 5)

Six new features were created to capture business-relevant signals.

| Feature | Formula | Rationale |
|---|---|---|
| `CLV` | `MonthlyCharges × Tenure` | Customer Lifetime Value — higher CLV customers may have more to lose by leaving |
| `ChargePerMonth` | `TotalCharges / (Tenure + 1)` | Payment efficiency — detects if a customer's actual monthly cost drifts from stated charge |
| `ChargeCategory` | Bins of `MonthlyCharges` [0–60, 60–120, 120–200] | Discretises continuous charge into low/mid/high tiers |
| `IsLongTerm` | `Tenure > median(Tenure)` → 1 else 0 | Binary flag for established vs new customers |
| `IsHighValue` | `CLV > 75th percentile(CLV)` → 1 else 0 | Binary flag for premium customers |
| `MonthlyTotalRatio` | `MonthlyCharges / (TotalCharges + 1)` | Captures discrepancy between expected and actual charges — anomalies may indicate billing issues |

**Feature Importances (Random Forest):**

| Rank | Feature | Importance |
|---|---|---|
| 1 | Tenure | 0.355 |
| 2 | ChargePerMonth | 0.157 |
| 3 | CLV | 0.116 |
| 4 | Contract_OE | 0.091 |
| 5 | MonthlyCharges | 0.070 |
| 6 | MonthlyTotalRatio | 0.069 |
| 7 | TotalCharges | 0.057 |
| 8 | IsLongTerm | 0.028 |

---

## Step 6 — Feature Selection (Day 6)

**Correlation Analysis:** Computed Pearson correlation matrix on engineered features. Highly correlated pairs noted:
- `CLV` and `TotalCharges`: expected (CLV is derived from charges × tenure)
- `IsLongTerm` and `Tenure`: expected (IsLongTerm is a binarisation of Tenure)

**Selected Features for Final Model (14 total):**
`Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract_OE`, `PaperlessBilling_LE`, `SeniorCitizen`, `CLV`, `ChargePerMonth`, `ChargeCategory`, `IsLongTerm`, `IsHighValue`, `MonthlyTotalRatio`, `PM_Credit_Card`, `PM_Electronic_Check`

`CustomerID` was dropped as a non-informative identifier.

---

## Step 7 — Pipeline Construction (Day 7)

A full `sklearn` Pipeline was built to ensure reproducibility and prevent data leakage.

```
Pipeline
├── ColumnTransformer (preprocessor)
│   ├── StandardScaler → [Tenure, MonthlyCharges, TotalCharges, CLV, ChargePerMonth, MonthlyTotalRatio]
│   └── passthrough    → [Contract_OE, PaperlessBilling_LE, SeniorCitizen, ...]
└── Classifier (RandomForestClassifier / GradientBoostingClassifier / LogisticRegression)
```

**Train / Test Split:** 80/20 with stratification on `Churn` to preserve class balance.

---

## Model Results Summary

| Model | CV AUC (5-fold) | Test AUC | Test Accuracy |
|---|---|---|---|
| **Random Forest** | **0.992 ± 0.005** | **0.9995** | **98%** |
| Gradient Boosting | 0.993 ± 0.003 | 0.987 | 95% |
| Logistic Regression | 0.973 ± 0.015 | 0.991 | 95% |

**Best Model:** Random Forest with AUC = 0.9995 on test set.

---

## Data Quality Summary

| Check | Status |
|---|---|
| Missing values | ✅ None |
| Duplicate rows | ✅ None detected |
| Outliers | ✅ None detected (IQR + Z-score) |
| Class imbalance | ⚠️ Mild (10.6% positive class) — handled via stratified splits |
| Encoding completeness | ✅ All categoricals encoded |
