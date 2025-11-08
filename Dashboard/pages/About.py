import streamlit as st
from pathlib import Path
from Utils_Module import load_theme, inject_css_bg, render_title, render_box, render_button
from utils_ui_pages import render_side_menu


# Page configuration - MUST be first
st.set_page_config(page_title="About Us - Space Dashboard", layout="wide")

# Load the space theme
load_theme()

render_side_menu("logov3.png")

# Add space background image using local file
inject_css_bg("background.png")

# Display logo with sidebar menu
# render_side_menu()

# Hero Page Title - ABOUT (largest title at the top)
render_title("ABOUT", variant="page", align="center", glow=True)

# MBTI Intro section - Title OUTSIDE the box
render_title("MBTI INTRO", variant="section", align="center", glow=True)

# Content INSIDE the box with title and icon
render_box(
    title="What is MBTI? ",
    icon="🧠",
    body="""
The **Myers-Briggs Type Indicator** is a test that can help people identify their strengths, preferences, and personality type. It assesses four different aspects of someone’s personality to sort them into one of 16 different personality types. The 4 aspects are split into 2 letters, which are:

- **Extraversion (E) or Introversion (I)** – Where someone focuses their energy. 
- **Sensing (S) or INtuition (N)** – How someone takes in information.  
- **Thinking (T) or Feeling (F)** – How someone makes decisions. 
- **Judging (J) or Perceiving (P)**	How someone deals with the world. 
    """,
    variant="primary",
    size="lg",
    align="center",
    framed=True,
    markdown=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

# Dashboard Overview section - Title OUTSIDE the box
render_title("DASHBOARD OVERVIEW", variant="section", align="center", glow=True)

# Content INSIDE the box with title and icon
render_box(
    title="Explore Your Personality Universe",
    icon="🛰️",
    body="""
Digital Dynamics' interactive dashboard guides graduates throughout the preliminary stage of finding a relevant career, integrating the MBTI personality structure into being, along with an exciting space-themed experience. Users explore through immersive and relevant personality types, discovering:
- **Statistics:**
Users can interact with the bar chart, donut graph, and treemap, which display their personality distribution and job correlations. And, guests can compare their personality to others to see if there is a better-suited career for the way they are.
- **Personalities:**
Discovering 16 variations of MBTI personalities, each with a captivating representation that matches one's character. Guests can browse resources to find out more regarding MBTI and take a personality test.
- **Career Guidance:**
Based on the MBTI type, the users who choose the dashboard can provide insights on plausible career paths based on the data, which takes into account. Users can also choose specific jobs, although it is not relevant to their personality

Set out on your journey by knowing your personality for a better future!

    """,
    variant="purple",
    size="lg",
    align="center",
    framed=True,
    markdown=True
)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# Call-to-action button
if render_button("READY TO EXPLORE", key="explore_btn", variant="primary", position="center"):
    st.success("🚀 Launching into the personality universe...")
    # Add navigation logic here, for example:
    st.switch_page("pages/explore.py")

import streamlit as st

# --- Back button style ---
st.markdown("""
<style>
.back-btn-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
    width: 100%;
}
div[data-testid="stButton"] > button[kind="secondary"].back-btn {
    background: linear-gradient(90deg, #00BFFF 0%, #007BFF 100%) !important;
    color: #E6F3FF !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 1.2rem 3rem !important;
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.2rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    text-shadow: 0 0 8px rgba(255,255,255,0.75);
    box-shadow: 0 0 25px #00BFFF, 0 0 60px #007BFF !important;
    transition: transform .25s ease, box-shadow .25s ease !important;
}
div[data-testid="stButton"] > button[kind="secondary"].back-btn:hover {
    transform: scale(1.08) !important;
    box-shadow: 0 0 40px #00BFFF, 0 0 90px #007BFF !important;
}
</style>
""", unsafe_allow_html=True)

# --- Centered Back button ---
st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
if st.button("← BACK", key="back-btn"):
    st.switch_page("home_pagev5.py")
st.markdown('</div>', unsafe_allow_html=True)