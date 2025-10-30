import streamlit as st

# theme testing
from utils_ui import load_theme
st.set_page_config(page_title="Font Test", layout="wide")
from utils_ui import render_title

# call function 
load_theme()
render_title("MBTI CAREER QUEST", variant="hero", align="center", glow=True)
render_title("Career Matches", variant="page", glow=False)
render_title("Filters", variant="section", align="left")
render_title("Explore Careers", variant="page", size=80)
st.write("this is normal text")



# testing 
st.markdown("<h1 style='font-family: Orbitron; color: cyan;'>Testing Orbitron Font</h1>", unsafe_allow_html=True)

st.write("Hopefully it works!")

# test background 
from utils_ui import inject_css_bg
inject_css_bg("background.png")

# button testing 
from utils_ui import render_button
if render_button("Start your Journey"): 
    st.success("Journey Started!")

render_button("Back", position="left")


col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    render_button("Start", key="start_left")
with col3:
    render_button("Exit", key="exit_right", variant="secondary")

st.markdown('<button class="btn-hero">Start Your Journey</button>', unsafe_allow_html=True)

# simple box (markdown body)
from utils_ui import render_box
render_box(
    title="Filters",
    icon="",
    body="""
- Choose *MBTI* type
- Select preferred **industry**
- Toggle **experience level** 
""",
    variant="primary",
    size="sm",
    align="left",
    framed=True,
    markdown=False
)

# larger info panel
render_box(
    title="Career Matches",
    icon="",
    body="<p>Top matches are generated using your MBTI + skills. Click a role to see required skills and learning path.</p>",
    variant="primary",
    size="lg",
    align="center", 
    markdown=False
)

# raw HTML body example (markdown=False)
render_box(
    title="Reminder",
    icon="",
    body="<p>Save favorites and compare salaries across regions.\n What is more?\n\n Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next  </p>", 
    variant="green",
    size="lg",
    align="left",
    framed=True,
    markdown=False
)

render_box(
    title="Another",
    icon="",
    body="<p>Save favorites and compare salaries across regions.\n What is more?\n\n Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next Next  </p>", 
    variant="green",
    size="lg",
    align="center",
    framed=True,
    markdown=False
)