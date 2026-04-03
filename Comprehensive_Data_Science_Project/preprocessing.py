"""
src/preprocessing.py
Data preprocessing utilities for the capstone project.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler


def load_and_preprocess_churn(filepath: str):
    """Load customer churn data and return features/target."""
    df = pd.read_csv(filepath)
    le = LabelEncoder()
    for col in ['Contract', 'PaymentMethod', 'PaperlessBilling']:
        df[f'{col}_enc'] = le.fit_transform(df[col])

    features = [
        'Tenure', 'MonthlyCharges', 'TotalCharges',
        'Contract_enc', 'PaymentMethod_enc', 'PaperlessBilling_enc', 'SeniorCitizen'
    ]
    X = df[features]
    y = df['Churn']
    return X, y, df


def load_and_preprocess_house(filepath: str):
    """Load house price data and return features/target."""
    df = pd.read_csv(filepath)
    le2, le3 = LabelEncoder(), LabelEncoder()
    df['Location_enc'] = le2.fit_transform(df['Location'])
    df['PropertyType_enc'] = le3.fit_transform(df['Property_Type'])

    features = ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Location_enc', 'PropertyType_enc']
    X = df[features]
    y = df['Price']
    return X, y, df


def load_and_preprocess_sales(filepath: str) -> pd.DataFrame:
    """Load and enrich sales data."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Month_Name'] = df['Date'].dt.month_name()
    df['Week'] = df['Date'].dt.isocalendar().week.astype(int)
    return df


def validate_data_quality(df: pd.DataFrame, name: str) -> dict:
    """Return a data quality report for a dataframe."""
    report = {
        "dataset": name,
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }
    return report
