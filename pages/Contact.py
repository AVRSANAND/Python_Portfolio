import streamlit as st
from send_email import send_email

st.title("Contact Me")

st.write("Email: avrsanand2003@gmail.com")

st.write("LinkedIn: [AVRSANAND](https://www.linkedin.com/in/avrsanand/)")

st.write("GitHub: [AVRSANAND](https://github.com/AVRSANAND)")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message...")
    user_message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        send_email(user_message)
        st.info("Your email was sent successfully! Thank you!")
