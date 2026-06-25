import streamlit as st

from utils import load_data

df = load_data()

st.title("Business Insights")

top_state = (
    df.groupby("State")["Sales"]
    .sum()
    .idxmax()
)

top_category = (
    df.groupby("Category")["Profit"]
    .sum()
    .idxmax()
)

top_segment = (
    df.groupby("Segment")["Sales"]
    .sum()
    .idxmax()
)

st.success(
    f"Top State: {top_state}"
)

st.success(
    f"Top Category: {top_category}"
)

st.success(
    f"Top Segment: {top_segment}"
)

st.markdown("""
### Recommendations

- Focus marketing on high-profit categories.
- Expand operations in top-performing states.
- Review loss-making orders.
- Improve shipping efficiency.
""")