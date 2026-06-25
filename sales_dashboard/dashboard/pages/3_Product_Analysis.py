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