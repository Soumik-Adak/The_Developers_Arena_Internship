# Sales Data Analysis Project
# Description: Load, clean, and analyze sales data using pandas

import pandas as pd

# === Step 1: Load Data ===
df = pd.read_csv("sales_data.csv")

# === Step 2: Explore Data ===
print("First 5 rows of the dataset:")
print(df.head(), "\n")

print("Data Types:")
print(df.dtypes, "\n")

print("Null Values Check:")
print(df.isnull().sum(), "\n")

print("Duplicate Rows Count:")
print(df.duplicated().sum(), "\n")

# === Step 3: Clean Data ===
# Drop duplicates if any
df = df.drop_duplicates()

# Handle missing values (if any) — here we simply drop them
df = df.dropna()

# === Step 4: Analysis ===
# Total revenue
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Best-selling product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
best_product_sales = df.groupby('Product')['Total_Sales'].sum().max()
print(f"Best-Selling Product: {best_product} (₹{best_product_sales:,.2f})")

# Regional sales distribution
regional_sales = df.groupby('Region')['Total_Sales'].sum()
print("\n Regional Sales Distribution:")
print(regional_sales)