import streamlit as st

st.set_page_config(layout="wide")

st.title("Welcome to my personal portfolio")
# st.write("Will be adding all the python related projects in here :)")

# st.write("Check out my [GitHub](https://github.com/avrsanand)")
# st.write("Check out my [LinkedIn](https://www.linkedin.com/in/avrsanand/)")
# st.subheader("Python Simple Todo App")
# st.subheader("Zip Archive creator & extractor")

col1, col2 = st.columns(2)

with col1:
    st.image("images/avrsanand.jpg")

with col2:
    st.title("AVRS ANAND")
    content = """
    Hi, I am Anand! I am a Python programmer, and I love to build projects. 
    I am currently learning and experimenting various things in python.  
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. 
Feel free to contact me throught any of the social media apps such as Linkedln, Twitter (X), Instagram etc.. Cheers!
"""
st.write(content2)
