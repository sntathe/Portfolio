import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/passport.JPG")

with col2:
    st.title("Saket Tathe")
    content = """
    Hi , I am Saket Tathe 
    I am trying to do python programming.
    This is my portfolio app
    """
    st.info(content)

st.write("Below are the App I have developed in Python. Feel free to contact me!")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
