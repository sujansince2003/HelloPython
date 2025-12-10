from model import UserSignup
from pydantic import ValidationError
from service import create_user
import streamlit as st


st.title("Signup form")
username = st.text_input("Enter the username")
email = st.text_input("Enter the email")
password = st.text_input("Enter the password", type="password")
age = st.number_input("Enter your age", min_value=16, max_value=40)
if st.button("Signup"):
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "age": age,
    }

    try:
        user = UserSignup(**user_data)
        st.success("User data is valid!")
        response = create_user(user)
        st.success(f"User created successfully! User ID: {response['user_id']}")

    except ValidationError as e:
        st.error(f"Error creating user: {e}")
