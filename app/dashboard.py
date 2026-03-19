import streamlit as st
import pandas as pd

st.set_page_config(page_title="Flowlytics Dashboard", layout="wide")

st.title("📊 Flowlytics Dashboard")

try:
    df = pd.read_csv("data/processed/final.csv")

    st.subheader("📋 Data Preview")
    st.dataframe(df)

    if 'total' in df.columns:
        st.subheader("📈 Total Sales Chart")
        st.bar_chart(df['total'])

except Exception as e:
    st.error("⚠️ Data not found. Run pipeline first.")