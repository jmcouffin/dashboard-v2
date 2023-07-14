import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
 
# Add Title
st.title("Use Pygwalker In Streamlit with BIMOne Data")


path = "https://drive.google.com/uc?id=1xrg4HFhb6oHuG7tU0ZB6SFyv3eksETcI"
df = pd.read_csv(path, parse_dates=['date'], dayfirst=True, encoding_errors='ignore')
df = df.sort_values('date')
 
# Generate the HTML using Pygwalker
pyg_html = pyg.walk(df, return_html=True)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)