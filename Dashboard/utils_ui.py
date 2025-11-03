import streamlit as st 
import base64
from pathlib import Path
from html import escape
from streamlit_extras.switch_page_button import switch_page
import uuid


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

    /* === Space Panel / Text Box ============================== */
    .ui-box {
    --accent:#00BFFF;                 /* default cyan accent */
    --bg:rgba(10,15,30,.55);
    --border:rgba(0,191,255,.35);
    --glow:0 0 18px rgba(0,191,255,.45);
    width:100%;
    border-radius:18px;
    padding:1rem 1.25rem;
    border:1px solid var(--border);
    background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)), var(--bg);
    backdrop-filter: blur(6px);
    box-shadow: var(--glow);
    position:relative;
    overflow:hidden;
    }

    /* decorative corner notches */
    .ui-box:before, .ui-box:after{
    content:"";
    position:absolute; inset:auto 18px 18px auto;
    width:42px; height:10px; border:1px solid var(--border); border-top:none; border-left:none;
    opacity:.6; border-radius:0 0 8px 0;
    }
    .ui-box:after{ inset:18px auto auto 18px; border-top:1px solid var(--border); border-right:none; border-bottom:none; border-radius:8px 0 0 0; height:10px; width:42px; }

    /* header */
    .ui-box .ui-box__title{
    display:flex; align-items:center; gap:.6rem;
    font-weight:900; letter-spacing:.06em;
    margin:0 0 .35rem 0;
    color:#E6F3FF;
    text-shadow: 0 0 10px rgba(0,191,255,.45);
    }
    .ui-box .ui-box__icon{ filter: drop-shadow(0 0 10px rgba(0,191,255,.5)); }

    /* content */
    .ui-box .ui-box__content{ color:#E6F3FF; 
    line-height:1.6;
    font-stretch: condensed; 
    letter-spacing: 0.08em;
    font-weight: 400; }

    /* sizes */
    .ui-box.sm{ max-width:520px; }
    .ui-box.md{ max-width:820px; }
    .ui-box.lg{ max-width:1180px; }

    /* variants (just swap accent color) */
    .ui-box.primary { --accent:#00BFFF; --border:rgba(0,191,255,.35); --glow:0 0 18px rgba(0,191,255,.45); }
    .ui-box.purple  { --accent:#9F7AEA; --border:rgba(159,122,234,.35); --glow:0 0 18px rgba(159,122,234,.45); }
    .ui-box.pink    { --accent:#FF6AD5; --border:rgba(255,106,213,.35); --glow:0 0 18px rgba(255,106,213,.45); }
    .ui-box.green   { --accent:#34D399; --border:rgba(52,211,153,.35); --glow:0 0 18px rgba(52,211,153,.45); }

    /* optional framed style like your sample image */
    .ui-box.frame{
    background: rgba(12,18,34,.6);
    border:2px solid var(--border);
    box-shadow: 0 0 0 2px rgba(255,255,255,.04) inset, var(--glow);
    padding:1.2rem 1.4rem;
    border-radius:22px;
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

def render_box(
    body: str,
    title: str | None = None,
    icon: str | None = None,              # e.g., "🛰️" or "<img ...>"
    variant: str = "primary",             # "primary" | "purple" | "pink" | "green"
    size: str = "md",                     # "sm" | "md" | "lg"
    align: str = "center",                # "left" | "center" | "right"
    framed: bool = False,                 # adds thicker frame style
    markdown: bool = True                 # treat body as Markdown
):
    # pick alignment column
    if align == "left":
        col = st.columns([1, 2, 3])[0]
    elif align == "right":
        col = st.columns([3, 2, 1])[2]
    else:
        col = st.columns([1, 2, 1])[1]

    with col:
        # assemble HTML
        classes = f"ui-box {variant} {size}" + (" frame" if framed else "")
        title_html = ""
        if title:
            if icon and not icon.strip().startswith("<"):
                icon_html = f"<span class='ui-box__icon'>{escape(icon)}</span>"
            else:
                icon_html = (icon or "")
            title_html = f"<div class='ui-box__title'>{icon_html}<span>{escape(title)}</span></div>"

        if markdown:
            # allow Streamlit markdown inside
            st.markdown(f"<div class='{classes}'>{title_html}<div class='ui-box__content'>", unsafe_allow_html=True)
            st.markdown(body)  # body can contain **markdown**, lists, etc.
            st.markdown("</div></div>", unsafe_allow_html=True)
        else:
            # raw HTML body
            st.markdown(f"<div class='{classes}'>{title_html}<div class='ui-box__content'>{body}</div></div>", unsafe_allow_html=True)



def _data_uri(path: str):
    p = Path(path)
    mime = "image/png" if p.suffix.lower()==".png" else "image/jpeg"
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def render_side_menu(logo_path="logov3.png"):
    # --- toggle via query param  ---
    qp = st.query_params
    if "toggle_menu" in qp:
        st.session_state["menu_open"] = not st.session_state.get("menu_open", False)
        st.query_params.clear()
    if "menu_open" not in st.session_state:
        st.session_state["menu_open"] = False

    # --- fixed logo button (single element) ---
    logo_uri = _data_uri(logo_path) 
    st.markdown(
        f"""
        <a class="mcq-menu-logo" href="?toggle_menu=1"></a>
        <style>
          .mcq-menu-logo {{
            position: fixed; top: 18px; left: 18px; z-index: 1000;
            width: 64px; height: 64px; display:block; border-radius: 50%;
            background: url("{logo_uri}") center/cover no-repeat;
            border: 2px solid rgba(0,191,255,.35);
            box-shadow: 0 0 18px rgba(0,191,255,.45);
            transition: transform .25s ease, box-shadow .25s ease;
          }}
          .mcq-menu-logo:hover {{ transform: scale(1.06); box-shadow: 0 0 26px rgba(0,191,255,.85); }}

          /* hide Streamlit's built-in nav + collapse button */
          [data-testid="stSidebarNav"] {{ display:none !important; }}
          [data-testid="stSidebarCollapseButton"] {{ display:none !important; }}
          section[data-testid="stSidebar"] [title="Close sidebar"] {{ display:none !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

    if not st.session_state["menu_open"]:
        st.markdown('<style>section[data-testid="stSidebar"]{display:none!important;}</style>', unsafe_allow_html=True)
        return
    

    st.markdown("""
    <style>
    section[data-testid="stSidebar"] > div {
        background: #000000 !important;   /* solid black */
        border-right: 1px solid rgba(0,191,255,0.25); /* optional cyan border */
    }
    [data-testid="stSidebar"] a {
    color: #FFFFFF !important;
    text-decoration: none !important;
    font-weight: 600;
    }

    /* hover glow effect */
    [data-testid="stSidebar"] a:hover {
    color: #00BFFF !important;      /* neon blue hover */
    text-shadow: 0 0 8px rgba(0,191,255,0.7);
    }
    </style>
    """, unsafe_allow_html=True)

    # menu 
    with st.sidebar:
        st.image(logo_path, width=96)  
        st.markdown("### MBTI Career Quest")
        st.page_link("pages/main.py", label="HOME")
        st.page_link("pages/homepagev1.py", label="ABOUT")
        st.page_link("pages/HomePagev4.py", label="EXPLORE")

        st.markdown(
            """
            <style>
            .close-btn {
            background-color:#000000 !important;
            color: #FFFFFF;
            border:1px solid rgba(255,255,255,.15) !important;
            font-family:'Orbitron',ui-sans-serif !important;
            font-weight:700 !important;
            font-size:16px !important;
            border-radius:10px !important;
            transition:all .25s ease !important;
            }
            .close-btn:hover {
            color:#00BFFF !important;
            border-color:rgba(0,191,255,.4) !important;
            box-shadow:0 0 12px rgba(0,191,255,.45) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        

        if st.button("CLOSE", key="nav-close", help="Close Menu"):
            st.session_state["menu_open"] = False