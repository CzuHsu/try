import pandas as pd
import streamlit as st

a = pd.read_csv("sentiment_summary拷貝.csv")
st.title("Hello World!")
st.write(a)