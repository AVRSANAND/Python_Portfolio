import streamlit as st
from send_email import send_email

st.title("Contact Me")

st.write("Email: avrsanand2003@gmail.com")

st.write("LinkedIn: [AVRSANAND](https://www.linkedin.com/in/avrsanand/)")

st.write("GitHub: [AVRSANAND](https://github.com/AVRSANAND)")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message...")
    user_message = user_message + "\n" + user_email
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        send_email(user_message)