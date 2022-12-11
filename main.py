import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kunal Rai")
    content = """ Hi, I am Kunal! I am a Python programmer, Ethical Hacker, teacher, and founder of GreyCode.
    I love to write code and check system security 
    """
    st.write(content)