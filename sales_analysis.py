import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/ecommerce_sales_10000-2.csv")

# Check data
print(df.head())

# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print("Duplicate rows:", df.duplicated().sum())

# Check data types
print(df.dtypes)

# Data Cleaning
df["Discount"] = df["Discount"].fillna(0)

df = df.dropna(subset=["Product", "Region"])

df = df.drop_duplicates()

# Final check
print("Cleaning completed")
print("Duplicate rows:", df.duplicated().sum())
print(df.isnull().sum())

# Basic Sales Analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Best Category
category_sales = df.groupby("Category")["Sales"].sum()
print("Best Category:", category_sales.idxmax())

# Best Region
region_sales = df.groupby("Region")["Sales"].sum()
print("Best Region:", region_sales.idxmax())

# Top Product
product_sales = df.groupby("Product")["Sales"].sum()
print("Top Product:", product_sales.idxmax())

# Category-wise Sales Chart

plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("category_sales.png")
plt.show()

# Region-wise Sales Chart

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("region_sales.png")
plt.show()

# Monthly Sales Trend

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = df.groupby(
    df["Order_Date"].dt.to_period("M")
)["Sales"].sum()

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales.png")
plt.show()




# Top 5 Products

top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title("Top 5 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("top_5_products.png")
plt.show()

# Final Business Insights

print("\n--- Business Insights ---")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Best Category:", category_sales.idxmax())
print("Best Region:", region_sales.idxmax())
print("Top Product:", product_sales.idxmax())