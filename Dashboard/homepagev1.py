import base64
from io import BytesIO
import textwrap
import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="MBTI Career Quest",
    page_icon="🧭",
    layout="wide",
)

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
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


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