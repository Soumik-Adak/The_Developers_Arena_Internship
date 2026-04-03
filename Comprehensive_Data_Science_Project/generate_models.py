"""
generate_models.py
Run this script ONCE to train all models and save the .pkl files.
Place this file in the same folder as app.py, then run:
    python generate_models.py
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib

# ── Paths ────────────────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, 'data')       # folder containing your CSVs
OUT  = BASE                              # save .pkl files next to app.py

os.makedirs(DATA, exist_ok=True)

# ── Helper ───────────────────────────────────────────────
def find_csv(name):
    """Look for the CSV in ./data/ or in the same folder as this script."""
    candidates = [
        os.path.join(DATA, name),
        os.path.join(BASE, name),
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    raise FileNotFoundError(
        f"\n[ERROR] Could not find '{name}'.\n"
        f"Please put it in:  {DATA}\n"
        f"or next to this script:  {BASE}\n"
    )

# ════════════════════════════════════════════════════════
# 1. CHURN MODEL
# ════════════════════════════════════════════════════════
print("Training churn model...")
churn_path = find_csv('customer_churn.csv')
churn = pd.read_csv(churn_path)

le = LabelEncoder()
for col in ['Contract', 'PaymentMethod', 'PaperlessBilling']:
    churn[f'{col}_enc'] = le.fit_transform(churn[col])

CHURN_FEATURES = [
    'Tenure', 'MonthlyCharges', 'TotalCharges',
    'Contract_enc', 'PaymentMethod_enc', 'PaperlessBilling_enc', 'SeniorCitizen'
]
X_c = churn[CHURN_FEATURES]
y_c = churn['Churn']

X_ctr, X_cte, y_ctr, y_cte = train_test_split(
    X_c, y_c, test_size=0.2, random_state=42, stratify=y_c
)
scaler = StandardScaler()
X_ctr_s = scaler.fit_transform(X_ctr)
X_cte_s = scaler.transform(X_cte)

churn_model = RandomForestClassifier(n_estimators=100, random_state=42)
churn_model.fit(X_ctr_s, y_ctr)

joblib.dump(churn_model, os.path.join(OUT, 'churn_model.pkl'))
joblib.dump(scaler,      os.path.join(OUT, 'scaler.pkl'))
print(f"  Saved churn_model.pkl")
print(f"  Saved scaler.pkl")

# ════════════════════════════════════════════════════════
# 2. HOUSE PRICE MODEL
# ════════════════════════════════════════════════════════
print("Training house price model...")
house_path = find_csv('house_prices.csv')
house = pd.read_csv(house_path)

le2, le3 = LabelEncoder(), LabelEncoder()
house['Location_enc']    = le2.fit_transform(house['Location'])
house['PropertyType_enc']= le3.fit_transform(house['Property_Type'])

HOUSE_FEATURES = ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Location_enc', 'PropertyType_enc']
X_h = house[HOUSE_FEATURES]
y_h = house['Price']

X_htr, X_hte, y_htr, y_hte = train_test_split(X_h, y_h, test_size=0.2, random_state=42)
house_model = RandomForestRegressor(n_estimators=100, random_state=42)
house_model.fit(X_htr, y_htr)

joblib.dump(house_model, os.path.join(OUT, 'house_model.pkl'))
print(f"  Saved house_model.pkl")

# ════════════════════════════════════════════════════════
# DONE
# ════════════════════════════════════════════════════════
print("\nAll models generated successfully!")
print(f"Files saved to: {OUT}")
print("\nYou can now run:  python app.py")
