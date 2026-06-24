import streamlit as st
import pandas as pd

from prophet import Prophet
import plotly.graph_objects as go

df = pd.read_csv("data/sales data.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
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

monthly.columns = ["ds","y"]

model = Prophet()

model.fit(monthly)

future = model.make_future_dataframe(
    periods=6,
    freq="M"
)

forecast = model.predict(future)

st.title("Sales Forecast")

fig = go.Figure()

fig.add_scatter(
    x=monthly["ds"],
    y=monthly["y"],
    name="Actual"
)

fig.add_scatter(
    x=forecast["ds"],
    y=forecast["yhat"],
    name="Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)