import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/sales data.csv")

st.title("Customer Analysis")

segment = (
    df.groupby("Segment")
    .agg({
        "Sales":"sum",
        "Profit":"sum"
    })
    .reset_index()
)

fig = px.bar(
    segment,
    x="Segment",
    y="Sales",
    title="Sales by Segment"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(
        "Sales",
        ascending=False
    )
    .head(10)
)

fig2 = px.bar(
    customers,
    x="Sales",
    y="Customer Name",
    orientation="h",
    title="Top Customers"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)