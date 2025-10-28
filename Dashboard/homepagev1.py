import base64
from io import BytesIO
import textwrap
import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="MBTI Career Quest",
    page_icon="",  # place holder for now
    layout="wide",
    )
# 1) Load Google Fonts via <link> (more reliable than @import)
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ---------------------------
# Helpers
# ---------------------------

def _b64_image(file_bytes: bytes) -> str:
    return base64.b64encode(file_bytes).decode()


def set_background(image_bytes: bytes | None = None, image_url: str | None = None, blur_px: int = 0, dim: float = 0.0):
    # Build the image layer
    bg_layer = ""
    if image_bytes:
        b64 = base64.b64encode(image_bytes).decode()
        bg_layer = f"url('data:image/png;base64,{b64}')"
    elif image_url:
        bg_layer = f"url('{image_url}')"

    # Build layers only if present
    layers = []
    if bg_layer:
        if dim > 0:
            layers.append(f"linear-gradient(rgba(0,0,0,{dim}), rgba(0,0,0,{dim}))")
        layers.append(bg_layer)

    bg_value = ", ".join(layers) if layers else "none"

    css = f"""
    <style>

    .stApp {{
        background-image: {bg_value};
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
    }}

    
    /* Title */
    .hero-title {{
        font-family: 'Orbitron', sans-serif;
        font-weight: 800;
        text-align: center;
        color: #E6F3FF;
        font-size: clamp(100px, 8vw, 120px);
        text-shadow:
            3px 3px 0 #007BFF,
            6px 6px 0 #00BFFF,
            9px 9px 15px rgba(0,191,255,0.6),
            0 0 30px rgba(255,255,255,0.9);
    letter-spacing: 0.1em;
    animation: glow 2s ease-in-out infinite alternate;
    margin-bottom: 3rem; /* ⬅ Adjust spacing between title and button */
}}

    @keyframes glow {{
        from {{ text-shadow: 0 0 15px #00BFFF, 0 0 30px #E6F3FF, 0 0 45px #1E90FF }}
        to {{ text-shadow: 0 0 25px #E6F3FF, 0 0 50px #00BFFF, 0 0 70px #87CEFA }}
    }}

    .center-screen {{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        flex-direction: column;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# button styles
st.markdown("""
<style>
/* Hero button (special for homepage) */
.btn-hero {
  font-family: 'Orbitron', sans-serif;
  font-weight: 700;
  font-size: 1.0rem;
  color: #E6F3FF;
  background: linear-gradient(90deg, #007BFF 0%, #00BFFF 100%);
  border: none;
  border-radius: 50px;
  padding: 1.2rem 3rem;
  margin-top: 2rem;
  cursor: pointer;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  box-shadow: 0 0 20px #00BFFF, 0 0 40px #007BFF;
  transition: all 0.3s ease-in-out;
}

.btn-hero:hover {
  transform: scale(1.08);
  box-shadow: 0 0 30px #00BFFF, 0 0 60px #007BFF;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------
# Default background 
# ---------------------------
DEFAULT_BG_PATH = "background.png"  
default_bg_bytes = None
try:
    with open(DEFAULT_BG_PATH, "rb") as f:
        default_bg_bytes = f.read()
except Exception:
    # No default file found; that's okay
    pass

try:
    with open(DEFAULT_BG_PATH, "rb") as f:
        default_bg_bytes = f.read()
    set_background(image_bytes=default_bg_bytes, blur_px=4, dim=0.25)
except Exception as e:
    st.write("bg error:", e)


# Hero Title in Center
# ---------------------------
st.markdown(
    """
    <div class="center-screen">
        <h1 class="hero-title" style="font-family:'Orbitron', sans-serif;">MBTI QUEST</h1>
        <button class="btn-hero">Start Your Journey</button>
    </div>
    """,
    unsafe_allow_html=True,
)