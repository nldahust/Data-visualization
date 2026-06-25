import streamlit as st
import plotly.express as px

from utils import load_data

df = load_data()

st.title("Customer Analysis")

segment = (
    df.groupby("Segment")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    segment,
    names="Segment",
    values="Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

customer = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    customer,
    x="Customer Name",
    y="Sales"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)