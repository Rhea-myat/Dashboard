import streamlit as st

# page config
st.set_page_config(
    page_title="MBTI Career Quest",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Session state for demo navigation
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "HOME"

# ----------------------
# Custom Fonts & Theme CSS
# ----------------------
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet">
    <style>
        /* Background */
        .stApp {
            background: url("background.png") no-repeat center center fixed;
            background-size: cover;
        }
        /* Titles */
        .title-arcade {
            font-family: 'Press Start 2P', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            letter-spacing: 2px;
            text-align: center;
            font-size: clamp(28px, 4vw, 42px);
            color: #ffffff;
            text-shadow: 0 0 8px rgba(255,255,255,.35), 0 0 24px rgba(163, 73, 255, .45);
            margin: 6px 0 8px 0;
        }
        .subtitle-arcade {
            font-family: 'VT323', monospace;
            text-align: center;
            font-size: clamp(16px, 2.2vw, 22px);
            color: rgba(255,255,255,.85);
            margin-bottom: 22px;
        }

        /* Neon Button (used for Start Game) */
        .neon-btn {
            font-family: 'Press Start 2P', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            padding: 16px 26px;
            border-radius: 14px;
            border: 2px solid rgba(255,255,255,.25);
            background: linear-gradient(90deg, #ff37f5 0%, #ff7493 100%);
            color: #fff !important;
            text-shadow: 0 1px 0 rgba(0,0,0,.25);
            box-shadow: 0 6px 18px rgba(255, 105, 180, .35), inset 0 0 12px rgba(255,255,255,.15);
            transition: transform .06s ease, box-shadow .2s ease, filter .2s ease;
            display: inline-block;
            text-decoration: none;
        }
        .neon-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 26px rgba(255, 105, 180, .55), inset 0 0 12px rgba(255,255,255,.25);
            filter: brightness(1.06);
        }

        /* Style Streamlit buttons globally to match the neon theme */
        .stButton > button {
            font-family: 'Press Start 2P', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            padding: 16px 26px;
            border-radius: 14px;
            border: 2px solid rgba(255,255,255,.25);
            background: linear-gradient(90deg, #ff37f5 0%, #ff7493 100%) !important;
            color: #fff !important;
            text-shadow: 0 1px 0 rgba(0,0,0,.25);
            box-shadow: 0 6px 18px rgba(255, 105, 180, .35), inset 0 0 12px rgba(255,255,255,.15);
            transition: transform .06s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 26px rgba(255, 105, 180, .55), inset 0 0 12px rgba(255,255,255,.25);
            filter: brightness(1.06);
        }

        /* ---- Tabs styling to mimic neon START GAME theme ---- */
        div[data-baseweb="tab-list"] > div[role="tab"] {
            font-family: 'Press Start 2P', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            padding: 12px 18px;
            margin: 0 8px 10px 0;
            border-radius: 12px;
            border: 2px solid rgba(255,255,255,.25);
            background: linear-gradient(90deg, #ff37f5, #ff7493);
            color: #fff;
            text-shadow: 0 1px 0 rgba(0,0,0,.25);
            box-shadow: 0 6px 18px rgba(255, 105, 180, .35), inset 0 0 12px rgba(255,255,255,.12);
            transition: transform .06s ease, box-shadow .2s ease, filter .2s ease;
        }
        div[data-baseweb="tab-list"] > div[role="tab"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 26px rgba(255, 105, 180, .55), inset 0 0 12px rgba(255,255,255,.2);
        }
        /* Selected tab gets brighter + white border */
        div[data-baseweb="tab-list"] > div[role="tab"][aria-selected="true"] {
            border-color: rgba(255,255,255,.65);
            filter: brightness(1.08);
        }

        /* Card-like panels */
        .panel {
            border-radius: 18px;
            padding: 24px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.18);
            box-shadow: 0 6px 30px rgba(0,0,0,0.25), inset 0 0 16px rgba(255,255,255,0.06);
        }
        .panel h3, .panel p, .panel li {
            color: rgba(255,255,255,.92) !important;
            font-family: 'VT323', monospace;
            font-size: 20px;
        }
        .footer-note {
            text-align:center;
            color: rgba(255,255,255,0.7);
            font-family: 'VT323', monospace;
            margin-top: 26px;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------
# Header
# ----------------------
st.markdown('<div class="title-arcade">MBTI CAREER QUEST</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-arcade">Discover Your Perfect Career Path Through Data</div>', unsafe_allow_html=True)

# ----------------------
# Tabs
# ----------------------
tab_home, tab_dashboard, tab_about = st.tabs([">>> HOME <<<", ">>> DASHBOARD <<<", ">>> ABOUT <<<"])

with tab_home:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    c = st.container()
    with c:
        st.write("")
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            start_clicked = st.button(">>> START GAME <<<", use_container_width=True)
        st.write("")
        st.markdown(
            """
            <div style="text-align:center; margin-top: 12px; font-family:'VT323', monospace; color: rgba(255,255,255,.85); font-size: 20px;">
                Myers–Briggs Type Indicator × Career Insights
            </div>
            """,
            unsafe_allow_html=True
        )

        if start_clicked:
            st.session_state.active_tab = "DASHBOARD"
            st.success("Starting game… (navigate to the DASHBOARD tab to continue)")

    st.markdown("</div>", unsafe_allow_html=True)

with tab_dashboard:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h3>Interactive Dashboard (Placeholder)</h3>
        <p>
        This is where your Streamlit charts, filters, and insights will live.
        Connect your dataset and render views like:
        </p>
        <ul>
            <li>Type distribution and trait breakdown</li>
            <li>Top careers by MBTI dimension</li>
            <li>Skills vs. personality heatmaps</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.info("Tip: Import your charts into this tab when your data pipeline is ready.")
    st.markdown("</div>", unsafe_allow_html=True)

with tab_about:
    st.markdown("<div class='panel'>", unsafe_allow_html=True)
    st.markdown(
        """
        <h3>About MBTI</h3>
        <p>
        MBTI is a personality framework built on 4 key dimensions:
        </p>
        <ul>
            <li>Energy: Introversion (I) vs Extraversion (E)</li>
            <li>Information: Sensing (S) vs Intuition (N)</li>
            <li>Decisions: Thinking (T) vs Feeling (F)</li>
            <li>Lifestyle: Judging (J) vs Perceiving (P)</li>
        </ul>
        <p>
        Use this app as a fun, data-informed way to explore possible career paths aligned
        with your personality preferences.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------
# Footer
# ----------------------
st.markdown('<div class="footer-note">© 2025 MBTI Career Quest · Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)

