import streamlit as st 
from utils_ui_pages import load_theme, inject_css_bg, render_title, render_anim, render_button, render_side_menu
import random


# page config
st.set_page_config(
    page_title="MBTI Career Quest", 
    page_icon="logov3.png",
    layout="wide",
)

# theme + background 
load_theme()
inject_css_bg("background.png")

render_side_menu()
#astronut on top of title
render_anim("astronut", 
            "https://lottie.host/embed/d27b2045-0670-4c4f-afb6-2cd399ebbee3/QeiQKtPvLe.lottie", 
            left="42%",
            top="1vh",
            transform="translateX(-50%)",
            width="220px",
            height="220px",
            )

st.markdown("<div>", unsafe_allow_html=True)
# Page title and sub title
st.markdown("""
<style>
.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 15vh;
  position: relative;
  text-align: center;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='home-page'>", unsafe_allow_html=True)
render_title("MBTI CAREER QUEST", variant="page", align="center", glow=True)
render_title("Find Out Your Best Job!", variant="section")
render_anim("stars", "https://lottie.host/embed/abde8ba3-6551-4f3b-9097-c8032d113f0e/gaKDGGxoam.lottie", right="1vw", width="1000px", height="1000px")
st.markdown("</div>", unsafe_allow_html=True)


# start button
# --- Style and center the hero button ---
st.markdown("""
<style>
/* Center wrapper */
div[data-testid="stButton"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    margin-top: 2.5rem !important;
}

/* Button styling */
div[data-testid="stButton"] > button[kind="secondary"] {
    background: linear-gradient(90deg, #007BFF 0%, #00BFFF 100%) !important;
    color: #E6F3FF !important;
    border: none !important;
    border-radius: 60px !important;
    padding: 1.5rem 4rem !important;          /* increased size */
    font-family: 'Orbitron', sans-serif !important;
    font-weight: 900 !important;
    font-size: 1.6rem !important;             /* bigger text */
    text-transform: uppercase !important;
    letter-spacing: 0.14em !important;
    box-shadow: 0 0 35px #00BFFF, 0 0 80px #007BFF !important;
    transition: transform .3s ease, box-shadow .3s ease !important;
}

/* Hover effect */
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    transform: scale(1.12) !important;
    box-shadow: 0 0 45px #00BFFF, 0 0 100px #007BFF !important;
}
</style>
""", unsafe_allow_html=True)

# --- Centered button that links to Explore ---
col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button(" ✨ START YOUR JOURNEY HERE ✨ ", key="start-btn"):
        st.switch_page("pages/About.py")

st.markdown("</div>", unsafe_allow_html=True)
# animations 
astronaut = "https://lottie.host/embed/d27b2045-0670-4c4f-afb6-2cd399ebbee3/QeiQKtPvLe.lottie"
cat = "https://lottie.host/embed/3a469622-a7b7-4e93-9c61-a9eb41721e01/Nn5OCwm6ai.lottie"
starts = "https://lottie.host/embed/abde8ba3-6551-4f3b-9097-c8032d113f0e/gaKDGGxoam.lottie"

# pick random positions each time the page runs
left = random.randint(5, 70)   # 5vw–70vw horizontally
top  = random.randint(20, 70)  # 20vh–70vh vertically

render_anim("cat",
            "https://lottie.host/embed/3a469622-a7b7-4e93-9c61-a9eb41721e01/Nn5OCwm6ai.lottie",
            width="1500px", height="1500px", bottom="1vh", right="5vh", seconds=random.randint(6,10),rotate = random.randint(-15, 15))





