import streamlit as st
import pandas as pd

# Load dataset
ds = pd.read_csv("ds_salaries_clean.csv")

st.title("Data Science Salaries Dataset")
st.write("Dataset Preview")
st.dataframe(ds)

st.write("Basic Statistics")
st.write(ds.describe())