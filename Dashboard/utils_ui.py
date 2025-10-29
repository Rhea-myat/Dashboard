import streamlit as st 
import base64
from pathlib import Path

def load_theme():
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">


    <style>
    /* 1) Apply Orbitron to ALL Streamlit elements (texts + widgets) */
    .stApp, .stApp * {
    font-family: 'Orbitron', sans-serif !important;
    }

    :root {
    --title-color: #E6F3FF;
    --glow-a: #007BFF;
    --glow-b: #00BFFF;
    }

    @keyframes glow {
    from { text-shadow: 0 0 15px #00BFFF, 0 0 30px #E6F3FF, 0 0 45px #1E90FF; }
    to   { text-shadow: 0 0 25px #E6F3FF, 0 0 50px #00BFFF, 0 0 70px #87CEFA; }
    }

    /* Base title */
    .title {
    font-family: 'Orbitron', sans-serif;
    font-weight: 1000;
    color: var(--title-color);
    letter-spacing: .08em;
    margin: 0 auto;
    }
    .title.glow { animation: glow 2s ease-in-out infinite alternate; }

    .title-hero   { font-size: clamp(72px, 8vw, 120px);  margin-top: 120px;  margin-bottom: 2.5rem; }
    .title-page   { font-size: clamp(36px, 5vw, 64px);   margin-top: 48px;   margin-bottom: 1.5rem; }
    .title-section{ font-size: clamp(24px, 3.5vw, 36px); margin-top: 24px;   margin-bottom: 1rem; }

    .t-center { text-align: center; }
    .t-left   { text-align: left; }
    .t-right  { text-align: right; }

    .title-hero {
    text-shadow:
        3px 3px 0 var(--glow-a),
        6px 6px 0 var(--glow-b),
        9px 9px 15px rgba(0,191,255,.6),
        0 0 30px rgba(255,255,255,.9);
    }


    /* === BASE BUTTON STYLE (for all Streamlit buttons) === */
    .stButton > button {
    background: linear-gradient(90deg, #007BFF, #00BFFF);
    color: #E6F3FF !important;
    border: none;
    border-radius: 50px;
    padding: 0.9rem 2rem;
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 0 20px #00BFFF, 0 0 40px #007BFF;
    }

    .stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px #00BFFF, 0 0 70px #007BFF;
    }

    /* === HERO BUTTON (for homepage main call-to-action) === */
    .btn-hero {
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    font-size: 1.3rem;
    color: #E6F3FF;
    background: linear-gradient(90deg, #007BFF 0%, #00BFFF 100%);
    border: none;
    border-radius: 50px;
    padding: 1.2rem 3rem;
    margin-top: 2rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    box-shadow: 0 0 25px #00BFFF, 0 0 60px #007BFF;
    transition: all 0.3s ease-in-out;
    }

    .btn-hero:hover {
    transform: scale(1.08);
    box-shadow: 0 0 35px #00BFFF, 0 0 80px #007BFF;
    }

    /* === SECONDARY (OUTLINE) BUTTON === */
    .secondary-btn > button {
    background: transparent !important;
    border: 2px solid #00FFFF !important;
    color: #E6F3FF !important;
    box-shadow: none !important;
    }

    .secondary-btn > button:hover {
    background: rgba(0,255,255,0.1) !important;
    box-shadow: 0 0 20px #00FFFF !important;
    }

    </style>
    """, unsafe_allow_html=True)

def render_title(text, variant="page", align="center", glow=True, size=None):
    vmap = {"hero":"title-hero", "page":"title-page", "section":"title-section"}
    amap = {"left":"t-left", "center":"t-center", "right":"t-right"}
    style = f"style='font-size:{size}px;'" if size else ""
    classes = f"title {vmap.get(variant,'title-page')} {amap.get(align,'t-center')}{' glow' if glow else ''}"
    st.markdown(f"<h1 class='{classes}' {style}>{text}</h1>", unsafe_allow_html=True)




def inject_css_bg(img_path_or_url: str):
    # if it's a web URL, use it directly
    if img_path_or_url.startswith(("http://", "https://")):
        bg_url = img_path_or_url
    else:
        # read local file and embed as base64 data URI
        p = Path(img_path_or_url)
        if not p.exists():
            st.warning(f"Background image not found: {p.resolve()}")
            return
        ext = p.suffix.lower().lstrip(".") or "png"
        mime = f"image/{'jpeg' if ext in ('jpg','jpeg') else ext}"
        data = base64.b64encode(p.read_bytes()).decode("utf-8")
        bg_url = f"data:{mime};base64,{data}"

    st.markdown(
        f"""
        <style>
        /* App background */
        .stApp {{
            background: url('{bg_url}') center / cover fixed no-repeat;
        }}
        /* Make main block transparent so bg is visible */
        .block-container {{
            background: transparent !important;
        }}
        /* Optional: transparent header */
        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}
        /* Optional: transparent sidebar */
        section[data-testid="stSidebar"] > div {{
            background: rgba(0,0,0,0);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def render_button(label: str, key: str | None = None, center: bool = True):
    if center:
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            return st.button(label, key=key)
    else:
        return st.button(label, key=key)

    # emulate a simple click detection using Streamlit's session state
    return st.button(label, key=f"{btn_id}_internal")

# 2. Render centered button
# ----------------------------
def render_button(label: str, key: str = None, variant: str = "primary"):
    """
    Creates a centered glowing button with consistent styling.
    - label: button text
    - key: Streamlit key
    - variant: 'primary' or 'secondary'
    """
    # Center alignment using columns
    left, center, right = st.columns([1, 2, 1])
    with center:
        if variant == "secondary":
            with st.container():
                st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
                clicked = st.button(label, key=key)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            clicked = st.button(label, key=key)
    return clicked

def render_button(label: str, key: str = None, variant: str = "primary", position: str = "center"):
    """
    Renders a styled Streamlit button with optional position:
    position: 'left', 'center', or 'right'
    """
    # Define column layout based on position
    if position == "center":
        left, col, right = st.columns([1, 2, 1])
    elif position == "right":
        left, col, right = st.columns([2, 2, 1])
        col = right
    elif position == "left":
        left, col, right = st.columns([1, 2, 2])
        col = left
    else:
        col = st

    with col:
        if variant == "secondary":
            st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
            clicked = st.button(label, key=key)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            clicked = st.button(label, key=key)
    return clicked