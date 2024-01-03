import streamlit as st

st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Saket Tathe")
    content = """
    Hi , I am Saket Tathe 
    I am trying to do python programming.
    This is my portfolio app
    """
    st.info(content)
