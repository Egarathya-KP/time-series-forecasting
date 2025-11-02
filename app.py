import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Time Series Forecasting")

st.write("Upload your dataset below to visualize and forecast data.")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    st.write("### Line Chart")
    st.line_chart(df[df.columns[-1]])

st.markdown("Made with ❤️ using Streamlit")
