import streamlit as st

st.title("🌐 Persistent Streamlit App")
st.write("This app runs from Streamlit Cloud — always accessible online!")

# Text input to get user's name
name = st.text_input("Enter your name")

# Button to display message
if st.button("Click me"):
    if name:
        st.success(f"Hello, {name}! 👋 Welcome to your app.")
    else:
        st.warning("Please enter your name before clicking.")
