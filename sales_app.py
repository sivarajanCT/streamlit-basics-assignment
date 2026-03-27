import streamlit as st
import pandas as pd

st.title("Sales Summary Dashboard")
st.subheader("Interactive filter for product sales by category")

data = {
    "Product": [
        "Laptop Pro",
        "Wireless Mouse",
        "USB Hub",
        "Keyboard",
        "Speaker",
    ],
    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Accessories",
        "Electronics",
    ],
    "Sales": [12000, 4500, 2300, 3200, 7100]
}

df = pd.DataFrame(data)

categories = df["Category"].dropna().unique().tolist()
selected_category = st.sidebar.selectbox(
    "Filter by Category", options=["All"] + categories
)

if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

st.dataframe(filtered_df)

st.line_chart(
    filtered_df, x="Product", y="Sales", use_container_width=True
)