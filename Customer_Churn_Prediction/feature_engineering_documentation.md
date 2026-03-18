# Feature Engineering Documentation
## Customer Churn Prediction Project

---

## Overview

Starting from 9 raw columns, this project engineers **7 new features** that capture customer behavior patterns not directly observable from raw data. Each feature is grounded in business intuition about churn drivers.

---

## Feature 1 — Customer Lifetime Value (CLV)

**Formula:** `CLV = Tenure × MonthlyCharges`

**Business Rationale:**  
CLV estimates the total revenue trajectory a customer represents. Higher CLV customers are both more valuable to retain and potentially more price-sensitive. CLV approximates total spend trajectory better than TotalCharges alone (which is backward-looking).

**Statistics:** Range [30, 13,124] | Mean 4,087 | Std 3,093

**Churn Insight:** Churned customers have significantly lower CLV, validating it as a strong predictor.

```python
df['CLV'] = df['Tenure'] * df['MonthlyCharges']
```

---

## Feature 2 — Charge Per Month (Historical Average)

**Formula:** `ChargePerMonth = TotalCharges / (Tenure + 1)`

**Business Rationale:**  
MonthlyCharges captures the current rate; TotalCharges / Tenure gives the historical average monthly spend. A divergence between these (current charges rising vs. historical average) signals pricing pressure — a key churn driver.

```python
df['ChargePerMonth'] = df['TotalCharges'] / (df['Tenure'] + 1)
```

---

## Feature 3 — Charge Category (Value Tier)

**Formula:** Tertile binning of MonthlyCharges → Low (0) / Medium (1) / High (2)

**Business Rationale:**  
Customers cluster into pricing tiers with different churn sensitivity. Encoding tiers directly helps tree models exploit non-linear pricing boundaries.

```python
df['ChargeCategory'] = pd.qcut(df['MonthlyCharges'], q=3, labels=[0, 1, 2])
```

---

## Feature 4 — IsLongTerm (Tenure Flag)

**Formula:** `IsLongTerm = 1 if Tenure > median(Tenure) else 0`  
**Threshold:** 37 months (dataset median)

**Business Rationale:**  
Tenure is the most predictive raw feature. A binary flag above/below median creates a simple, interpretable loyalty signal that helps linear models detect threshold effects.

```python
df['IsLongTerm'] = (df['Tenure'] > df['Tenure'].median()).astype(int)
```

---

## Feature 5 — IsHighValue (CLV Flag)

**Formula:** `IsHighValue = 1 if CLV > 75th percentile(CLV) else 0`  
**Threshold:** CLV > 6,041

**Business Rationale:**  
High-value customers (top 25% by CLV) represent disproportionate revenue. Flagging them explicitly lets the model apply different learned weights to this cohort.

```python
df['IsHighValue'] = (df['CLV'] > df['CLV'].quantile(0.75)).astype(int)
```

---

## Feature 6 — Monthly-Total Ratio

**Formula:** `MonthlyTotalRatio = MonthlyCharges / (TotalCharges + 1)`

**Business Rationale:**  
Captures the recency weight of spending. A high ratio means recent monthly charges are high relative to historical total — suggesting bill increases. Customers experiencing bill shock churn more.

```python
df['MonthlyTotalRatio'] = df['MonthlyCharges'] / (df['TotalCharges'] + 1)
```

---

## Feature 7 — Senior High-Risk Flag

**Formula:** Binary = 1 if Senior + Month-to-month + MonthlyCharges > median

**Business Rationale:**  
Senior customers on monthly contracts with above-average bills form a specific high-risk cohort — less commitment inertia, higher financial pressure. Combines three conditions that individually have weaker signal, but jointly are strongly predictive.

```python
df['SeniorHighRisk'] = (
    (df['SeniorCitizen'] == 1) &
    (df['Contract'] == 'Month-to-month') &
    (df['MonthlyCharges'] > df['MonthlyCharges'].median())
).astype(int)
```

---

## Feature Importance Summary

| Feature | RF Importance | Type |
|---|---|---|
| Tenure | 0.3551 | Original |
| **ChargePerMonth** | **0.1569** | **Engineered** |
| **CLV** | **0.1163** | **Engineered** |
| Contract_OE | 0.0913 | Encoded |
| MonthlyCharges | 0.0700 | Original |
| **MonthlyTotalRatio** | **0.0690** | **Engineered** |
| TotalCharges | 0.0574 | Original |
| **IsLongTerm** | **0.0277** | **Engineered** |
| **ChargeCategory** | **0.0211** | **Engineered** |

Engineered features (`ChargePerMonth` rank 2, `CLV` rank 3) collectively account for ~38% of total feature importance.

---

## Notes

- **No data leakage:** All features are derived from attributes known at prediction time.
- **Multicollinearity:** CLV correlates with Tenure × MonthlyCharges — acceptable for tree-based models, monitored for Logistic Regression.
- **Scaling:** All engineered continuous features passed through StandardScaler in the pipeline.
