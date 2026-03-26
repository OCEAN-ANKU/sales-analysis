import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Sales Data Dashboard")

# Load Data
df = pd.read_csv("data/sales.csv")

# Show Data
st.subheader("Raw Data")
st.dataframe(df)

# Total Sales
st.subheader("Total Sales")
st.write(df["Sales"].sum())

# Sales by Product
st.subheader("Sales by Product")
product_sales = df.groupby("Product")["Sales"].sum()

fig, ax = plt.subplots()
product_sales.plot(kind="bar", ax=ax)
st.pyplot(fig)

# Profit by Region
st.subheader("Profit by Region")
region_profit = df.groupby("Region")["Profit"].sum()

fig2, ax2 = plt.subplots()
region_profit.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
st.pyplot(fig2)