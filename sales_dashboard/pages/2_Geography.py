import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/sales data.csv")

st.title("Geographic Analysis")

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    state_sales.sort_values(
        "Sales",
        ascending=False
    ).head(15),
    x="State",
    y="Sales",
    title="Top States by Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

region = (
    df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region,
    names="Region",
    values="Profit",
    title="Profit by Region"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)