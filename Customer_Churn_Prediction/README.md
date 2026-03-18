# Customer Churn Prediction Pipeline

## Project Overview

A complete 7-day machine learning project to predict customer churn using telecom data. The pipeline includes data exploration, categorical encoding, feature scaling, outlier detection, feature engineering, feature selection, and model evaluation.

**Final Model:** Random Forest | **Test ROC-AUC:** 0.9995 | **Accuracy:** 98%

---

## Project Structure

```
churn_prediction/
├── churn_prediction_pipeline.py       # Main pipeline script (all 7 days)
├── churn_data.csv                     # Raw dataset (500 customers)
├── churn_data_processed.csv           # Processed dataset with engineered features
├── preprocessing_report.md           # Full preprocessing documentation
├── feature_engineering_documentation.md  # Feature engineering rationale
├── requirements.txt                   # Python dependencies
└── visualizations/
    ├── eda_analysis.png               # Day 1: EDA overview
    ├── scaling_comparison.png         # Day 3: Scaling comparison
    ├── feature_importances.png        # Day 6: Feature importance
    ├── confusion_matrix.png           # Day 7: Confusion matrix
    ├── roc_curves.png                 # Day 7: ROC curves
    └── model_performance.png         # Day 7: Model comparison
```

---

## Setup Instructions

### 1. Clone / Download the Repository

```bash
git clone <your-repo-url>
cd churn_prediction
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

```bash
python churn_prediction_pipeline.py
```

### 5. Launch Jupyter Notebook (Optional)

```bash
jupyter notebook churn_prediction_pipeline.ipynb
```

---

## Day-by-Day Guide

| Day | Focus | Key Outputs |
|---|---|---|
| Day 1 | Data Exploration | EDA charts, churn distribution |
| Day 2 | Categorical Encoding | Label, One-Hot, Ordinal encoding |
| Day 3 | Feature Scaling | StandardScaler, MinMaxScaler comparison |
| Day 4 | Outlier Detection | IQR and Z-score analysis |
| Day 5 | Feature Engineering | 7 new features (CLV, ChargePerMonth, etc.) |
| Day 6 | Feature Selection | Correlation, Mutual Info, RF Importance |
| Day 7 | Pipeline & Model | sklearn Pipeline, 3-model comparison |

---

## Key Results

### Encoding Methods Used
1. **Label Encoding** — PaperlessBilling (binary Yes/No)
2. **One-Hot Encoding** — PaymentMethod (nominal, 3 categories)
3. **Ordinal Encoding** — Contract (ordered: Month < 1yr < 2yr)

### Scaling Techniques Used
1. **Standard Scaling** — Z-score normalization (mean=0, std=1)
2. **Min-Max Scaling** — Bounded normalization [0, 1]

### Engineered Features
1. `CLV` — Customer Lifetime Value (Tenure × MonthlyCharges)
2. `ChargePerMonth` — Historical average monthly spend
3. `ChargeCategory` — Low/Medium/High pricing tier
4. `IsLongTerm` — Binary tenure flag (>37 months)
5. `IsHighValue` — Binary CLV flag (top 25%)
6. `MonthlyTotalRatio` — Bill recency signal
7. `SeniorHighRisk` — High-risk senior customer flag

### Model Comparison

| Model | CV ROC-AUC | Test ROC-AUC |
|---|---|---|
| Random Forest | 0.9916 ± 0.0051 | **0.9995** |
| Gradient Boosting | 0.9926 ± 0.0030 | 0.9867 |
| Logistic Regression | 0.9735 ± 0.0147 | 0.9908 |

---

## Technical Details

### Pipeline Architecture

```
Raw CSV → Feature Engineering → ColumnTransformer → Classifier → Predictions
                                    ├── StandardScaler (numerical)
                                    ├── OrdinalEncoder (contract)
                                    ├── OneHotEncoder (payment method)
                                    └── OrdinalEncoder (binary features)
```

### Class Imbalance Handling
- 10.6% churn rate (imbalanced dataset)
- Addressed with `class_weight='balanced'` in Random Forest and Logistic Regression
- Evaluated using ROC-AUC and Precision-Recall (not just accuracy)

### Validation Strategy
- Train/Test split: 80/20 with stratification
- 5-Fold Stratified Cross-Validation for robust performance estimation

---

## Data Source

Dataset: https://bit.ly/customer-churn-data

