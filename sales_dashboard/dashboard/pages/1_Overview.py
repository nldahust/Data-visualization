import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_data

df = load_data()

st.title("Overview")

sales = df["Sales"].sum()
profit = df["Profit"].sum()
orders = df["Order ID"].nunique()
qty = df["Quantity"].sum()

margin = (
    profit / sales * 100
)

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric(
    "Sales",
    f"${sales:,.0f}"
)

c2.metric(
    "Profit",
    f"${profit:,.0f}"
)

c3.metric(
    "Orders",
    f"{orders:,}"
)

c4.metric(
    "Quantity",
    f"{qty:,}"
)

c5.metric(
    "Margin %",
    f"{margin:.2f}"
)

monthly = (
    df.groupby(
        pd.Grouper(
            key="Order Date",
            freq="M"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

category = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)