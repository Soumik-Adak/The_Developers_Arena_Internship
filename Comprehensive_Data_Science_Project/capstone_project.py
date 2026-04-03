"""
============================================================
COMPREHENSIVE DATA SCIENCE CAPSTONE PROJECT
Business Intelligence & Predictive Analytics Suite
============================================================
Datasets: Customer Churn, House Prices, Sales Data
============================================================
"""

# ── PHASE 1: PROJECT SETUP ────────────────────────────────
# Business Problem:
#   1. Predict which telecom customers will churn (classification)
#   2. Estimate residential property prices (regression)
#   3. Identify sales trends & revenue drivers (analytics)
#
# Success Metrics:
#   • Churn model  : ROC-AUC > 0.85, Precision/Recall balance
#   • House model  : R² > 0.85, MAE < 15% of mean price
#   • Sales        : Revenue by product/region/month insights

# ── PHASE 2: IMPORTS & DATA LOADING ──────────────────────
import pandas as pd
import numpy as np
import json, joblib, warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, mean_absolute_error,
    mean_squared_error, r2_score
)

# Load datasets
churn = pd.read_csv('data/customer_churn.csv')
house = pd.read_csv('data/house_prices.csv')
sales = pd.read_csv('data/sales_data.csv')

print(f"Churn dataset  : {churn.shape}")
print(f"House dataset  : {house.shape}")
print(f"Sales dataset  : {sales.shape}")

# ── PHASE 3: EXPLORATORY DATA ANALYSIS ───────────────────

# --- 3A. Customer Churn EDA ---
print("\n=== CHURN EDA ===")
print(churn.describe())
print(f"Churn rate: {churn['Churn'].mean():.1%}")
print(f"Senior citizens: {churn['SeniorCitizen'].mean():.1%}")
print(churn.groupby('Contract')['Churn'].mean())

# --- 3B. House Prices EDA ---
print("\n=== HOUSE EDA ===")
print(house.describe())
print(house.groupby('Location')['Price'].mean().sort_values(ascending=False))
print(house.groupby('Property_Type')['Price'].mean().sort_values(ascending=False))

# --- 3C. Sales EDA ---
print("\n=== SALES EDA ===")
sales['Date'] = pd.to_datetime(sales['Date'])
sales['Month'] = sales['Date'].dt.month_name()
print(sales.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False))
print(sales.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False))

# ── PHASE 4: FEATURE ENGINEERING & MODEL DEVELOPMENT ─────

# --- 4A. Churn Model ---
le = LabelEncoder()
for col in ['Contract', 'PaymentMethod', 'PaperlessBilling']:
    churn[f'{col}_enc'] = le.fit_transform(churn[col])

CHURN_FEATURES = [
    'Tenure', 'MonthlyCharges', 'TotalCharges',
    'Contract_enc', 'PaymentMethod_enc', 'PaperlessBilling_enc', 'SeniorCitizen'
]
X_c, y_c = churn[CHURN_FEATURES], churn['Churn']
X_ctr, X_cte, y_ctr, y_cte = train_test_split(X_c, y_c, test_size=0.2, random_state=42, stratify=y_c)

scaler = StandardScaler()
X_ctr_s = scaler.fit_transform(X_ctr)
X_cte_s = scaler.transform(X_cte)

churn_model = RandomForestClassifier(n_estimators=100, random_state=42)
churn_model.fit(X_ctr_s, y_ctr)

y_pred_c = churn_model.predict(X_cte_s)
y_prob_c = churn_model.predict_proba(X_cte_s)[:, 1]

print("\n=== CHURN MODEL RESULTS ===")
print(f"ROC-AUC : {roc_auc_score(y_cte, y_prob_c):.4f}")
print(classification_report(y_cte, y_pred_c))
cv = cross_val_score(churn_model, X_c, y_c, cv=5, scoring='roc_auc')
print(f"CV ROC-AUC: {cv.mean():.4f} ± {cv.std():.4f}")

# --- 4B. House Price Model ---
le2, le3 = LabelEncoder(), LabelEncoder()
house['Location_enc'] = le2.fit_transform(house['Location'])
house['PropertyType_enc'] = le3.fit_transform(house['Property_Type'])

HOUSE_FEATURES = ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Location_enc', 'PropertyType_enc']
X_h, y_h = house[HOUSE_FEATURES], house['Price']
X_htr, X_hte, y_htr, y_hte = train_test_split(X_h, y_h, test_size=0.2, random_state=42)

house_model = RandomForestRegressor(n_estimators=100, random_state=42)
house_model.fit(X_htr, y_htr)
y_pred_h = house_model.predict(X_hte)

print("\n=== HOUSE PRICE MODEL RESULTS ===")
print(f"R²   : {r2_score(y_hte, y_pred_h):.4f}")
print(f"MAE  : ₹{mean_absolute_error(y_hte, y_pred_h):,.0f}")
print(f"RMSE : ₹{np.sqrt(mean_squared_error(y_hte, y_pred_h)):,.0f}")

# ── PHASE 5: DEPLOYMENT ───────────────────────────────────
joblib.dump(churn_model, 'deployment/churn_model.pkl')
joblib.dump(scaler,      'deployment/scaler.pkl')
joblib.dump(house_model, 'deployment/house_model.pkl')
print("\nModels saved to deployment/")

print("\n✓ Capstone pipeline complete.")
