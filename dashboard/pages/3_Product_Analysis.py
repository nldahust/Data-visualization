import streamlit as st
import plotly.express as px

from utils import load_data

df = load_data()

st.title("Product Analysis")

subcategory = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .reset_index()
)

fig = px.bar(
    subcategory,
    x="Sub-Category",
    y="Profit"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig2 = px.treemap(
    df,
    path=[
        "Category",
        "Sub-Category"
    ],
    values="Sales"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Product Name",
    y="Sales",
    title="Top 10 Products by Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

bottom_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
    .reset_index()
)

fig = px.bar(
    bottom_products,
    x="Product Name",
    y="Profit",
    title="Bottom 10 Products by Profit"
)

st.plotly_chart(
    fig,
    use_container_width=True
)