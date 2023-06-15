import streamlit as st



st.write("Enter search query:")

st.text_input("", label_visibility="collapsed")
st.button("Search")
