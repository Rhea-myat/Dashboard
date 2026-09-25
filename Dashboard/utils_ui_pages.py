import streamlit as st 
import base64
from pathlib import Path
from html import escape
import uuid
import re


APP_DIR = Path(__file__).resolve().parent


def _app_path(path: str | Path) -> Path:
    path = Path(path)
    return path if path.is_absolute() else APP_DIR / path


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
    margin-left: auto;
    margin-right: auto;
    line-height: 1.15;
    overflow-wrap: anywhere;
    }
    .title.glow { animation: glow 2s ease-in-out infinite alternate; }

    .title-hero   { 
        font-size: clamp(100px, 12vw, 160px) !important;  
        margin-top: 80px !important;  
        margin-bottom: 3rem !important;
        text-shadow: 3px 3px 0 var(--glow-a), 6px 6px 0 var(--glow-b), 9px 9px 15px rgba(0,191,255,.6), 0 0 30px rgba(255,255,255,.9) !important;
    }
    .title-page   { 
        font-size: clamp(2.5rem, 6vw, 4.75rem) !important;
        margin-top: 2rem !important;
        margin-bottom: 2.5rem !important;
    }
    .title-section{ 
        font-size: clamp(1.5rem, 3.5vw, 2.65rem) !important;
        margin-top: 3.5rem !important;
        margin-bottom: 1rem !important;
    }
    .title-description{
        font-size: clamp(0.95rem, 1.6vw, 1.2rem) !important;
        margin-top: 0.5rem !important;
        margin-bottom: 2.5rem !important;
        font-weight: 400 !important;
        line-height: 1.6;
        opacity: 0.9;
    }
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
    --bg:rgba(7,12,25,.88);
    --border:rgba(0,191,255,.35);
    --glow:0 0 18px rgba(0,191,255,.45);
    width:100%;
    border-radius:18px;
    padding:2rem 2.5rem;
    border:1px solid var(--border);
    background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)), var(--bg);
    backdrop-filter: blur(6px);
    box-shadow: var(--glow);
    position:relative;
    overflow:hidden;
    margin:0 auto 2rem;
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
    font-size:clamp(1.1rem, 2vw, 1.4rem);
    text-shadow: 0 0 10px rgba(0,191,255,.45);
    }
    .ui-box .ui-box__icon{ filter: drop-shadow(0 0 10px rgba(0,191,255,.5)); }

    /* content */
    .ui-box .ui-box__content{ color:#E6F3FF !important;
    line-height:1.7;
    font-stretch: condensed; 
    letter-spacing: 0.02em;
    font-weight: 400; }

    .ui-box .ui-box__content p,
    .ui-box .ui-box__content ul,
    .ui-box .ui-box__content ol {
    color:#E6F3FF !important;
    font-size:clamp(0.95rem, 1.25vw, 1.05rem) !important;
    line-height:1.7 !important;
    }
    .ui-box .ui-box__content p { margin:1rem 0 !important; }
    .ui-box .ui-box__content ul,
    .ui-box .ui-box__content ol { margin:1rem 0 !important; padding-left:2rem !important; }
    .ui-box .ui-box__content li { margin:.5rem 0 !important; color:#E6F3FF !important; }
    .ui-box .ui-box__content strong { font-size:inherit !important; color:#E6F3FF !important; }

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
    background: rgba(7,12,25,.9);
    border:2px solid var(--border);
    box-shadow: 0 0 0 2px rgba(255,255,255,.04) inset, var(--glow);
    padding:2rem 2.5rem;
    border-radius:22px;
    }

    @media (max-width: 768px) {
        .title-page { margin-top:1.25rem !important; margin-bottom:2rem !important; }
        .title-section { margin-top:2.5rem !important; margin-bottom:.75rem !important; }
        .title-description { margin-bottom:2rem !important; }
        .ui-box, .ui-box.frame { padding:1.25rem !important; }
        .ui-box .ui-box__content ul,
        .ui-box .ui-box__content ol { padding-left:1.3rem !important; }
    }
    </style>
    """, unsafe_allow_html=True)

def render_title(text, variant="page", align="center", glow=True, size=None):
    vmap = {"hero":"title-hero", "page":"title-page", "section":"title-section", "description":"title-description"}
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
        p = _app_path(img_path_or_url)
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

def _simple_markdown_to_html(text: str) -> str:
    """Convert panel paragraphs, lists, and bold text without extra packages."""
    blocks, paragraph, list_items = [], [], []

    def inline(value: str) -> str:
        safe = escape(value.strip())
        return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", safe)

    def flush_paragraph():
        if paragraph:
            blocks.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list():
        if list_items:
            blocks.append("<ul>" + "".join(f"<li>{inline(item)}</li>" for item in list_items) + "</ul>")
            list_items.clear()

    for raw_line in text.strip().splitlines():
        line = raw_line.strip()
        if line.startswith("- "):
            flush_paragraph()
            list_items.append(line[2:])
        elif not line:
            flush_paragraph()
            flush_list()
        else:
            flush_list()
            paragraph.append(line)
    flush_paragraph()
    flush_list()
    return "".join(blocks)


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
        col = st.columns([1, 8, 1])[1]

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

        body_html = _simple_markdown_to_html(body) if markdown else body
        st.markdown(
            f"<div class='{classes}'>{title_html}<div class='ui-box__content'>{body_html}</div></div>",
            unsafe_allow_html=True,
        )



def _data_uri(path: str):
    p = _app_path(path)
    mime = "image/png" if p.suffix.lower()==".png" else "image/jpeg"
    b64 = base64.b64encode(p.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


def render_side_menu(logo_path="assets/logov3.png"):
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
        st.page_link("pages/About.py", label="ABOUT")
        st.page_link("pages/explore.py", label="EXPLORE")
        st.page_link("pages/More.py", label="FIND OUT MORE")

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


def inject_anim_css(): 
    if st.session_state.get("_anim_css_injected"): 
        return 
    st.session_state["_anim_css_injected"]=True
    st.markdown(
        """
        <style>
        /* non-blocking overaly for lotties*/
        .mcq-overlay {position: fixed; inset: 0; pointer-events:none; z-index: 30; }
        .mcq-float {position: absolute; }
        .mcq-float iframe { width:100%;  height:100%; border:none; background:transparent; display:block; }
        .mcq-glow { filter: drop-shadow(0 0 18px rgba(0,180,255,.45));}

        /* float animation -duration is set per element via inline style  */
        @keyframe mcqFloat{
            0% {transform: translateY(0)}
            50% {transorm: translateY(-10px)}
            100% {transform: translateY(0)}
        }
         /* responsive tweaks per role */
        @media (max-width: 700px){
        .mcq-role-astronaut { width:160px !important; height:160px !important; right: 12px !important; top: 80px !important; }
        .mcq-role-cat       { width:140px !important; height:140px !important; right: 6vw  !important; bottom: 6vh !important; }
        .mcq-role-stars     { width:160px !important; height:160px !important; left:  4vw  !important; top:    8vh !important; }
      }
        </style>
        """, unsafe_allow_html=True
    )
    # role presets: position, size, glow, float speed
_PRESETS = {
    "astronaut": dict(right="20px", top="120px", width="260px", height="260px", glow=True, seconds=8),
    "cat":       dict(right="6vw",  bottom="8vh", width="220px", height="220px", glow=True, seconds=7),
    "stars":     dict(left="4vw",   top="10vh",   width="260px", height="260px", glow=True, seconds=9),
}


def render_anim(role: str, url:str, **overrides): 
    """
    render a lottie iframe with role-specific CSS presets
    role: 'astronut', 'cat', 'stars' 
    url: lottie.lottie/.json embed url 
    overrides: left/right/top/bottom/width/height/seconds/glow  --> str|int|bool
    """
    inject_anim_css()
    cfg = {**_PRESETS.get(role, {}), **overrides}

    # style pieces 
    pos = []
    for k in ("left","right","top","bottom"):
        v = cfg.get(k)
        if v is not None:
            pos.append(f"{k}:{v}")
    w = cfg.get("width", "220px")
    h = cfg.get("height","220px")
    secs = cfg.get("seconds", 8)
    glow = " mcq-glow" if cfg.get("glow", True) else ""

    st.markdown(f"""
    <div class="mcq-overlay">
      <div class="mcq-float mcq-role-{role}{glow}"
           style="{' ; '.join(pos)}; width:{w}; height:{h}; animation: mcqFloat {secs}s ease-in-out infinite;">
        <iframe src="{url}" allowfullscreen>

        </iframe>
      </div>
    </div>
    """, unsafe_allow_html=True)
