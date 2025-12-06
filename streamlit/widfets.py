import streamlit as st

age = st.text_input("Enter your age")
if age:
    agetype = type(age)
    st.text(agetype)
    st.write(age)

st.code("print('hello')", language="python")
