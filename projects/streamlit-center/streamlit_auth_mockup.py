"""
Streamlit Center - Authentication Module Mockup
Simple login form for screenshot purposes.
"""

import streamlit as st

st.set_page_config(
    page_title="Login - Streamlit Center",
    page_icon="🔐",
    layout="centered",
)

st.title("🔐 Streamlit Center")
st.markdown("### Please log in to continue")

st.divider()

with st.form("login_form"):
    username = st.text_input(
        "Username (corporate ID)",
        placeholder="Enter your username",
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
    )

    submitted = st.form_submit_button(
        "Log In", use_container_width=True, type="primary"
    )

    if submitted:
        if username and password:
            st.success("Login successful!")
        else:
            st.error("Please enter both username and password.")
