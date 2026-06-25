import pandas as pd
import numpy as np

INPUT_FILE = "../data/sales_data.csv"
OUTPUT_FILE = "../data/sales_processed.csv"

df = pd.read_csv(INPUT_FILE)

# Remove duplicates
df = df.drop_duplicates()

# Dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Time Features
df["Year"] = df["Order Date"].dt.year
df["Quarter"] = df["Order Date"].dt.quarter
df["Month"] = df["Order Date"].dt.month_name()
df["Month Number"] = df["Order Date"].dt.month

# Business Features
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

df["Profit Margin"] = np.where(
    df["Sales"] != 0,
    df["Profit"] / df["Sales"],
    0
)

df["Revenue Per Unit"] = np.where(
    df["Quantity"] != 0,
    df["Sales"] / df["Quantity"],
    0
)

df["Profit Per Unit"] = np.where(
    df["Quantity"] != 0,
    df["Profit"] / df["Quantity"],
    0
)

df["Loss Order"] = (
    df["Profit"] < 0
).astype(int)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("Saved:", OUTPUT_FILE)