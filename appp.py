import streamlit as st

name=st.text_input("enter your name")

st.title("take the input name")

if st.button("submit"):
   sr.write(f"print the name : (name)")
  
