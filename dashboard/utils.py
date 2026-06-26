import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "../data/sales_processed.csv"
    )

    df["Order Date"] = pd.to_datetime(
        df["Order Date"]
    )

    return df