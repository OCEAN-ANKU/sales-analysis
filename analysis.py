import pandas as pd

# Data load
df = pd.read_csv("data/sales.csv")

# Total Sales
print("Total Sales:", df["Sales"].sum())

# Sales by Product
print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

# Profit by Region
print("\nProfit by Region:")
print(df.groupby("Region")["Profit"].sum())