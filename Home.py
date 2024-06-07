import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Welcome to my personal portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("images/avrsanand.jpg")

with col2:
    st.title("AVRS ANAND")
    content = """
    Hi, I am Anand! 
    Welcome to my dedicated Python portfolio!
    
    I am a computer science graduate from the class of 2024, with a strong passion for programming and problem-solving. My journey in the tech world has led me to specialize in Python, a versatile and powerful language that I continually learn and experiment with.

    This portfolio showcases a variety of projects I've developed, ranging from simple scripts to more complex applications. Each project includes detailed descriptions and source codes, reflecting my commitment to writing clean, efficient, and well-documented code. I believe in continuous learning and regularly update my skills to keep pace with the ever-evolving tech landscape.

    In addition to Python, I am well-versed in other programming languages and technologies, which enables me to approach problems from different angles and provide robust solutions. My interest areas include data analysis, web development, and automation, and I am always on the lookout for new challenges to tackle.

    Feel free to explore my projects and get in touch if you have any questions or collaboration ideas. I am excited to share my work with you and look forward to connecting with fellow enthusiasts and professionals.
    """


    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. 
Feel free to contact me throught any of the social media apps such as Linkedln, Twitter (X), Instagram etc.. Cheers!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("current_data.csv", sep=";")

with col3:
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['git_url']})")
        st.write(f"[Live Demo]({row['live_url']})")

with col4:
    for index, row in df[1:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['git_url']})")
        st.write(f"[Live Demo]({row['live_url']})")
