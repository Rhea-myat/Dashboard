import streamlit as st

# page configuration
st.set_page_config(
    page_title= "MBTI Career Dashboard",
    page_icon= "🧙‍♂️", 
    layout= "centered",
)

# custom css for retro theme 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
    body {
        font-family: 'Press Start 2P', cursive;
        background-color: #000000;
        color: #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)
