import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/sales data.csv")

st.title("Product Analysis")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

subcat = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    subcat,
    x="Sub-Category",
    y="Profit",
    title="Profit by Sub-Category"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)