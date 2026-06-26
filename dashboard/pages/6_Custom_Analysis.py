import streamlit as st
import plotly.express as px

from utils import load_data

df = load_data()

st.title("Custom Analysis")

metric = st.selectbox(
    "Metric",
    [
        "Sales",
        "Profit",
        "Quantity",
        "Shipping Days"
    ]
)

dimension = st.selectbox(
    "Dimension",
    [
        "Region",
        "State",
        "City",
        "Category",
        "Sub-Category",
        "Segment",
        "Ship Mode"
    ]
)

chart = st.selectbox(
    "Chart Type",
    [
        "Bar",
        "Pie",
        "Line"
    ]
)

analysis = (
    df.groupby(dimension)[metric]
    .sum()
    .reset_index()
)

if chart == "Bar":

    fig = px.bar(
        analysis,
        x=dimension,
        y=metric
    )

elif chart == "Pie":

    fig = px.pie(
        analysis,
        names=dimension,
        values=metric
    )

else:

    fig = px.line(
        analysis,
        x=dimension,
        y=metric
    )

st.plotly_chart(
    fig,
    use_container_width=True
)