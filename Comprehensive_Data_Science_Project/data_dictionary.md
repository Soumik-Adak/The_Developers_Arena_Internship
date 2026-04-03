# Data Dictionary

## customer_churn.csv

| Column | Type | Description | Example |
|---|---|---|---|
| CustomerID | string | Unique customer identifier | C00001 |
| Tenure | int | Months as active customer | 24 |
| MonthlyCharges | int | Monthly billing amount (INR) | 80 |
| TotalCharges | int | Cumulative charges to date (INR) | 1920 |
| Contract | string | Contract type: Month-to-month, One year, Two year | One year |
| PaymentMethod | string | How customer pays: Bank transfer, Credit card, Electronic check, Mailed check | Credit card |
| PaperlessBilling | string | Whether paperless billing is enabled: Yes, No | Yes |
| SeniorCitizen | int | Whether customer is a senior citizen: 1=Yes, 0=No | 0 |
| Churn | int | Target variable — did customer churn: 1=Yes, 0=No | 0 |

## house_prices.csv

| Column | Type | Description | Example |
|---|---|---|---|
| Property_ID | string | Unique property identifier | PROP0001 |
| Area | int | Property area in square feet | 2500 |
| Bedrooms | int | Number of bedrooms (1–5) | 3 |
| Bathrooms | int | Number of bathrooms (1–3) | 2 |
| Age | int | Property age in years (0–49) | 10 |
| Location | string | Location tier: Rural, Suburb, Urban | Urban |
| Property_Type | string | Property classification: Apartment, House, Villa | House |
| Price | int | Market price in INR | 24500000 |

## sales_data.csv

| Column | Type | Description | Example |
|---|---|---|---|
| Date | string | Transaction date (YYYY-MM-DD) | 2024-01-01 |
| Product | string | Product sold: Phone, Headphones, Laptop, Tablet, Monitor | Laptop |
| Quantity | int | Units sold in transaction (1–9) | 3 |
| Price | int | Unit price in INR | 45000 |
| Customer_ID | string | Customer identifier | CUST001 |
| Region | string | Sales region: East, North, West, South | North |
| Total_Sales | int | Quantity × Price (INR) | 135000 |
