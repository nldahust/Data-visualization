import streamlit as st
import plotly.express as px

from utils import load_data

df = load_data()

st.title("Geography Analysis")

region = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    region,
    names="Region",
    values="Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

state = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
    .reset_index()
)

fig2 = px.bar(
    state,
    x="State",
    y="Sales",
    title="Top States"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)