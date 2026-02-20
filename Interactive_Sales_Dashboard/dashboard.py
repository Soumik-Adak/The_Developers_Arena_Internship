# Interactive Sales Dashboard
# Created by:Soumik Adak

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("sales_data.csv")

# -----------------------------
# 1. Sales Trend Over Time (Seaborn Line Plot)
# -----------------------------
plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Total_Sales", data=df, hue="Region", palette="Set2")
plt.title("Sales Trend by Region", fontsize=16)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 2. Price Distribution by Product (Seaborn Box Plot)
# -----------------------------
plt.figure(figsize=(10,6))
sns.boxplot(x="Product", y="Price", data=df, palette="pastel")
plt.title("Price Distribution by Product", fontsize=16)
plt.tight_layout()
plt.show()

# -----------------------------
# 3. Correlation Heatmap (Seaborn)
# -----------------------------
plt.figure(figsize=(8,6))
corr = df[["Quantity","Price","Total_Sales"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix", fontsize=16)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Interactive Product Performance (Plotly Bar Chart)
# -----------------------------
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()
plt.figure(figsize=(10,6))
plt.bar(product_sales["Product"], product_sales["Total_Sales"], color="skyblue", edgecolor="black")
plt.title("Total Sales by Product", fontsize=16)
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()


# -----------------------------
# 5. Interactive Scatter Plot (Plotly)
# -----------------------------
plt.figure(figsize=(10,6))
scatter = plt.scatter(df["Price"], df["Quantity"], 
                      c=df["Total_Sales"], cmap="viridis", alpha=0.7, s=50)

plt.colorbar(scatter, label="Total Sales")
plt.title("Price vs Quantity (Color = Total Sales)", fontsize=16)
plt.xlabel("Price")
plt.ylabel("Quantity")
plt.tight_layout()
plt.show()


# -----------------------------
# 6. Multi-Plot Dashboard Layout (Matplotlib Grid)
# -----------------------------
fig, axes = plt.subplots(2,2, figsize=(14,10))

sns.lineplot(x="Date", y="Total_Sales", data=df, ax=axes[0,0], color="blue")
axes[0,0].set_title("Sales Trend")

sns.barplot(x="Product", y="Total_Sales", data=df, ax=axes[0,1], palette="muted")
axes[0,1].set_title("Sales by Product")

sns.boxplot(x="Region", y="Total_Sales", data=df, ax=axes[1,0], palette="Set3")
axes[1,0].set_title("Sales Distribution by Region")

sns.violinplot(x="Product", y="Total_Sales", data=df, ax=axes[1,1], palette="husl")
axes[1,1].set_title("Sales Distribution by Product")

plt.tight_layout()
plt.show()