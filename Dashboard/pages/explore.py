import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from utils_ui_pages import load_theme, inject_css_bg, render_title, render_side_menu

st.set_page_config(page_title="Explore", layout="wide")
render_side_menu("logov3.png")

st.markdown("""
<style>
/* widen page */
.block-container { max-width: 1500px; padding-left: 2rem; padding-right: 2rem; }


/* Glow frame directly on Plotly charts */
[data-testid="stPlotlyChart"]{
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  margin: 0 !important;
}
[data-testid="stPlotlyChart"] > div { width: 100% !important; } /* ensure full width */


/* Do the same for tables if you show df.head() */
[data-testid="stDataFrame"] {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(0,191,255,0.35);
  border-radius: 16px;
  box-shadow: 0 0 18px rgba(0,191,255,0.45);
  padding: 12px;
  margin: 16px 0 32px 0;
}

/* section headings */
h1, h2, h3, h4 { color: #d4e7ff; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.nebula-card{
  display:block;
  width:100%;
  box-sizing:border-box;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(0,191,255,0.35);
  border-radius: 16px;
  box-shadow: 0 0 18px rgba(0,191,255,0.45);
  padding: 22px;
  margin: 28px 0;
}
h2, h3 { color:#d
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* === Cosmic Black Selectbox (Dropdown + Control) === */

/* Main select control */
.stSelectbox div[data-baseweb="select"] {
  background: #000 !important;  /* solid black box */
  border: 1px solid rgba(0,191,255,.6);
  border-radius: 12px;
  box-shadow: 0 0 18px rgba(0,191,255,.25);
  color: #E6F3FF;
  transition: box-shadow .25s ease, border-color .2s ease;
}

/* Inner elements (remove white background inside) */
.stSelectbox div[data-baseweb="select"] > div:first-child,
.stSelectbox div[data-baseweb="select"] div[role="combobox"],
.stSelectbox div[data-baseweb="select"] input {
  background: #000 !important;
  color: #E6F3FF !important;
}

/* Caret icon */
.stSelectbox div[data-baseweb="select"] svg {
  color: #00BFFF !important;
  fill: #00BFFF !important;
}

/* Hover + focus glow */
.stSelectbox div[data-baseweb="select"]:hover {
  border-color: #00E5FF;
  box-shadow: 0 0 25px rgba(0,229,255,.35);
}
.stSelectbox div[data-baseweb="select"]:focus-within {
  border-color: #00E5FF;
  box-shadow: 0 0 35px rgba(0,229,255,.45);
}

/* Dropdown (BaseWeb menu) */
div[data-baseweb="popover"] { background: transparent !important; }
div[data-baseweb="menu"] {
  background: #000 !important;  /* black dropdown background */
  border: 1px solid rgba(0,191,255,.45);
  border-radius: 12px;
  box-shadow: 0 12px 40px rgba(0,191,255,.25);
}

/* Options inside dropdown */
div[data-baseweb="menu"] [data-baseweb="option"] {
  color: #E6F3FF !important;      /* white text */
  font-family: 'Orbitron', sans-serif
  background: transparent !important;
}
div[data-baseweb="menu"] [data-baseweb="option"]:hover {
  background: rgba(0,191,255,.15) !important;
  font-family: 'Orbitron', sans-serif
}
div[data-baseweb="menu"] [aria-selected="true"] {
  background: linear-gradient(90deg, rgba(0,123,255,.35), rgba(0,191,255,.35)) !important;
  border-left: 3px solid #00E5FF;
}

/* Label styling */
.stSelectbox label {
  color:#9FB9FF !important;
  font-family:'Orbitron', sans-serif;
  text-shadow:0 0 8px rgba(0,191,255,.25);
  text-align:left !important;
  margin-left:0 !important;
  width:auto !important;
}

/* === Centered checkbox === */
    div[data-testid="stCheckbox"] {
      display:flex !important;
      justify-content:center !important;
    }
    div[data-testid="stCheckbox"] label p {
      color:#d4e7ff !important;
      font-size:0.85rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* === Reduce width of all Streamlit selectboxes === */
.stSelectbox div[data-baseweb="select"] {
  width: 40% !important;          /* 
  margin: 0 auto !important;      /* 🔹 keep it centered */
  border-radius: 10px !important;
}

/* Label styling */
.stSelectbox label {
  color:#9FB9FF !important;
  font-family:'Orbitron', sans-serif;
  text-shadow:0 0 8px rgba(0,191,255,.25);
  text-align:left !important;
  margin-left:0 !important;
  width:auto !important;
}

/* === Cosmic Slider (Top N Job Titles) === */
div[data-baseweb="slider"] {
  width: 35% !important;                  /* 🔹 reduce overall width */
  margin-left: 0 !important;              /* left-align under the select box */
}

[data-testid="stSlider"] {
  color: #00BFFF !important;
}

[data-testid="stSlider"] > div {
  background: transparent !important;
}

/* Track (line) styling */
[data-baseweb="slider"] > div:nth-child(1) {
  height: 6px !important;                 /* 🔹 thinner bar */
  background: rgba(0,191,255,0.35) !important;
  border-radius: 6px !important;
}

/* Active portion (filled track) */
[data-baseweb="slider"] > div:nth-child(1) > div {
  background: linear-gradient(90deg, #007BFF, #00BFFF) !important;
  box-shadow: 0 0 12px rgba(0,191,255,0.6);
}

/* Handle (draggable knob) */
[data-baseweb="slider"] span[data-baseweb="thumb"] {
  width: 18px !important;
  height: 18px !important;
  background: #00BFFF !important;
  box-shadow: 0 0 18px rgba(0,191,255,0.7);
  border: 2px solid #E6F3FF !important;
}

/* Label text (Top N Job Titles text) */
[data-testid="stWidgetLabel"] p {
  color: #9FB9FF !important;
  font-family: 'Orbitron', sans-serif;
  text-shadow: 0 0 8px rgba(0,191,255,0.25);
  font-size: 0.9rem !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_df(path="cleaned_kpmi_data.csv"):
    d = pd.read_csv(path)
    d.columns = d.columns.str.lower().str.strip()
    return d.rename(columns={
        "psychotype":"mbti",
        "jobfield":"job_field",
        "jobtitle":"job_title",
        "satisfied":"job_satisfaction"
    })

df = load_df()



# ---------- PIE: Overall / by Job Field ----------
def mbti_pie(df):
        st.subheader("Overall MBTI Distribution")
        fields = ["All"] + sorted(df["job_field"].dropna().unique().tolist())
        sel = st.selectbox("Filter by Job Field", fields, index=0)
        d = df if sel == "All" else df[df["job_field"] == sel]
        counts = d["mbti"].value_counts(dropna=False).reset_index()
        counts.columns = ["mbti","count"]
        cb1, cb2, cb3 = st.columns([1, 2, 1])
        with cb2:
            show_counts = st.checkbox("Show counts in labels", value=True, key="mbti_center_check")

        textinfo = "percent+label+value" if show_counts else "percent+label"

        fig = px.pie(counts, names="mbti", values="count", hole=0.3)
        fig.update_traces(textinfo=textinfo, pull=[0.03]*len(counts),
                        hovertemplate="<b>MBTI:</b> %{label}<br><b>Count:</b> %{value}<extra></extra>")
        fig.update_layout(
        legend=dict(
        x=0.92, y=0.5,
        xanchor="left", yanchor="middle",
        bgcolor="rgba(20,30,60,0.7)",          # semi-transparent dark background
        #bordercolor="rgba(0,191,255,0.4)",     # cyan border glow
        #borderwidth=1,
        font=dict(color="#d4e7ff")
        )
        )
        fig.update_layout(
            height=620,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(10,10,30,0.85)",
            font=dict(color="#d4e7ff"),
            legend_bgcolor="rgba(0,0,0,0.2)",
            legend_font=dict(color="#d4e7ff"),
            margin=dict(l=30, r=110, t=60, b=40),
        )
        st.plotly_chart(fig, use_container_width=True)



# ---------- TREEMAP: Job Field vs MBTI with satisfaction coloring ----------
def jobfield_treemap(df):
    st.subheader("MBTI Satisfaction Across Job Fields")
    d = df.dropna(subset=["job_field", "mbti", "job_satisfaction"]).copy()
    agg = (
        d.groupby(["job_field", "mbti"], as_index=False)
         .agg(Count=("job_satisfaction", "size"),
              Satisfaction=("job_satisfaction", "mean"))
    )

    # --- Move the selection box to the top ---
    fields = ["All Jobfields"] + sorted(agg["job_field"].unique().tolist())
    sel = st.selectbox("Select Jobfield", fields, index=0)  # <-- now above the chart

    def build_fig(data, title):
        fig = px.treemap(
            data,
            path=["job_field", "mbti"],
            values="Count",
            color="Satisfaction",
            color_continuous_scale="RdYlGn",
            range_color=(0, 1),
            hover_data={"job_field": False, "mbti": False, "Count": ":,", "Satisfaction": ":.2f"}
        )

        fig.update_traces(
            hovertemplate="<b>MBTI:</b> %{label}<br>"
                          "<b>Count:</b> %{value}<br>"
                          "<b>Satisfaction:</b> %{color:.2f}<extra></extra>",
            textfont=dict(color="#000000", size=13)
        )

        fig.update_layout(
        title=title,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(10,10,30,0.85)",
        font=dict(color="#d4e7ff", size=13),
        coloraxis_colorbar=dict(
        title=dict(
            text="Satisfaction",
            font=dict(color="#d4e7ff", size=13)
        ),
        tickfont=dict(color="#d4e7ff", size=11),
        thickness=12,   # same bar width
        len=0.6,        # same bar height (60% of plot)
        x=1.02,         # aligned horizontally
        y=0.5,          # vertically centered
        xpad=10,
        ypad=10,
        outlinewidth=0,
        bgcolor="rgba(0,0,0,0)",
        ),
        coloraxis=dict(cmin=0, cmax=1),  # <-- missing comma was here!
        margin=dict(l=20, r=20, t=40, b=20)
        )
        return fig

    # --- Display chart after selection ---
    if sel == "All Jobfields":
        st.plotly_chart(build_fig(agg, "All Jobfields Treemap and Satisfaction"), use_container_width=True)
    else:
        filtered = agg[agg["job_field"] == sel]
        st.plotly_chart(build_fig(filtered, f"{sel} Treemap and Satisfaction"), use_container_width=True)
        
# ---------- BAR: Job Satisfaction by MBTI ----------
def job_satisfaction_section(df):
    st.subheader("Different Version of Job Satisfaction of Each MBTI")

    # Dropdown for job fields
    fields = ["All Jobfields"] + sorted(df["job_field"].dropna().unique().tolist())
    sel = st.selectbox("Select Jobfield", fields, index=0, key="satisfaction_jobfield")

    # Filter data based on selection
    if sel == "All Jobfields":
        filtered = (
            df.groupby("mbti", as_index=False)
              .agg(Satisfaction=("job_satisfaction", "mean"))
        )
        title = "All Jobfields: Average Satisfaction by MBTI"
    else:
        filtered = (
            df[df["job_field"] == sel]
              .groupby("mbti", as_index=False)
              .agg(Satisfaction=("job_satisfaction", "mean"))
        )
        title = f"{sel}: Average Satisfaction by MBTI"

    # Create the bar chart
    fig = px.bar(
        filtered,
        x="mbti",
        y="Satisfaction",
        color="Satisfaction",
        color_continuous_scale="RdYlGn",
        title=title
    )

    # === Apply dark transparent background ===
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=60, r=30, l=30, b=40),
        plot_bgcolor="rgba(10,10,30,0.85)",   # dark glass effect
        paper_bgcolor="rgba(0,0,0,0)",        # transparent around edges
        font=dict(color="#d4e7ff", size=13),  # light text for readability
        coloraxis_colorbar=dict(
            title=dict(text="Satisfaction", font=dict(color="#d4e7ff")),
            tickfont=dict(color="#d4e7ff"),
            outlinewidth=0,
            bgcolor="rgba(0,0,0,0)"
        ), 
        coloraxis=dict(cmin=0, cmax=1)
    )

    # Slightly darken the grid lines
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255,255,255,0.1)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.1)")

    # Display
    st.plotly_chart(fig, use_container_width=True)

# ---------- BAR + TREEMAP: Job Title vs MBTI ----------
def job_title_vs_mbti(df):
    st.subheader("MBTI Satisfaction Across Job Fields")
    top_n = st.slider("Show Top N job titles", 10, 100, 30, step=5)
    top_titles = df["job_title"].value_counts().head(top_n).index
    d = df[df["job_title"].isin(top_titles)]
    grp = d.groupby(["job_title","mbti"]).size().reset_index(name="count")

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(grp, x="job_title", y="count", color="mbti",
                     barmode="group", title=f"MBTI across Top {top_n} Job Titles")
        fig.update_layout(xaxis_title="", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        tree = px.treemap(grp, path=["job_title","mbti"], values="count",
                          title=f"Job Title vs MBTI (Treemap) — Top {top_n}")
        st.plotly_chart(tree, use_container_width=True)

def _coerce_satisfaction(series):
    """Make job_satisfaction numeric in [0,1] where possible."""
    s = series.astype(str).str.strip().str.lower()
    map_yesno = {"yes":1, "no":0, "true":1, "false":0, "satisfied":1, "not satisfied":0}
    num = pd.to_numeric(s, errors="coerce")
    if num.notna().any():
        return (num - num.min()) / (num.max() - num.min()) if (num.max()!=num.min()) else (num*0)
    mapped = s.map(map_yesno)
    if mapped.notna().any():
        return mapped.fillna(np.nan).astype(float)
    # fallback: treat anything as categorical and not convertable (can't average)
    return pd.to_numeric(series, errors="coerce")


def jobtitle_mbti_satisfaction_bars(df, key_prefix="jt_bar"):
    st.subheader("Explore Job Title Vs MBTI Satisfaction")

    # Filter by job field
    fields = ["All"] + sorted(df["job_field"].dropna().unique().tolist())
    sel_field = st.selectbox("Filter by Job Field", fields, index=0, key=f"{key_prefix}_field")

    d = df if sel_field == "All" else df[df["job_field"] == sel_field].copy()
    d = d.dropna(subset=["job_title", "mbti", "job_satisfaction"])

    # Convert satisfaction to numeric [0,1]
    d["_sat_num"] = _coerce_satisfaction(d["job_satisfaction"])

    # Limit to top N job titles by sample size
    top_n = st.slider("Sllide To See Top Job Titles", min_value=10, max_value=33, value=30, step=5, key="jt_topn")
    st.markdown(
    f"<p style='color:#E6F3FF; font-family:Orbitron, sans-serif; font-size:0.9rem; "
    "text-shadow:0 0 8px rgba(0,191,255,0.3);'>"
    f"Showing top {top_n} job titles by frequency."
    "</p>",
    unsafe_allow_html=True
)

    top_titles = d["job_title"].value_counts().head(top_n).index
    d = d[d["job_title"].isin(top_titles)]

    # Aggregate data
    agg = (d.groupby(["job_title", "mbti"], as_index=False)
             .agg(count=("job_satisfaction", "size"),
                  avg_satisfaction=("_sat_num", "mean")))

    # --- Plotly grouped bar ---
    fig = px.bar(
        agg,
        x="job_title",
        y="count",
        color="avg_satisfaction",              # color intensity = avg satisfaction
        color_continuous_scale="RdYlGn",
        barmode="group",
        hover_data={
            "job_title": False,
            "mbti": True,
            "count": ":,",
            "avg_satisfaction": ":.2f"
        },
    )

    # Hover and styling
    fig.update_traces(
        customdata=agg[["mbti", "avg_satisfaction"]],
        hovertemplate=(
            "Job Title: %{x}<br>"
            "MBTI: %{customdata[0]}<br>"
            "Count: %{y:,}<br>"
            "Avg Satisfaction: %{customdata[1]:.2f}<extra></extra>"
        ),
        marker_line_width=0.3,
        marker_line_color="rgba(255,255,255,0.35)"
    )

    # === Cosmic theme ===
    fig.update_layout(
        title_x=0.5,
        height=750, 
        xaxis_tickangle=-45,
        margin=dict(t=80, r=60, l=80, b=260),
        plot_bgcolor="rgba(10,10,30,0.85)",    # dark glass-like background
        paper_bgcolor="rgba(0,0,0,0)",         # transparent behind
        font=dict(color="#d4e7ff", size=13),
        bargap=0.15,   # space between groups (default 0.2)
        bargroupgap=0.05,  # space within grouped bars
        
        coloraxis_colorbar=dict(
        title=dict(
            text="Satisfaction", 
            font=dict(color="#d4e7ff", size=13)
        ),
        tickfont=dict(color="#d4e7ff", size=11),
        thickness=12,   # same bar width
        len=0.6,        # same bar height (60% of plot)
        x=1.02,         # aligned horizontally
        y=0.5,          # vertically centered
        xpad=10,
        ypad=10,
        outlinewidth=0,
        bgcolor="rgba(0,0,0,0)"
    ),
    coloraxis=dict(
        cmin=0, cmax=1   # 🔹 Ensures same 0–1 satisfaction color range everywhere
    )
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True, theme=None)

load_theme()
inject_css_bg("background.png")


render_title("Explore", variant="title")
# ---------- Page body (hook these into your buttons/sections) ----------
st.markdown("<h4 style='text-align:center'>Discover your ideal career paths</h4>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
# Example flow (replace with your button logic):


mbti_pie(df)   # your chart call

st.markdown("<br><br><br>", unsafe_allow_html=True)
jobfield_treemap(df)
st.markdown("<br>", unsafe_allow_html=True)
job_satisfaction_section(df)  # or pass your precomputed agg_all
st.markdown("<br>", unsafe_allow_html=True)
jobtitle_mbti_satisfaction_bars(df, key_prefix="jt2")



# --- Back & Next Button Styles ---
st.markdown("""
<style>
.nav-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 3rem;
    padding: 0 6rem; /* controls left-right spacing */
}

/* Shared style for both buttons */
div[data-testid="stButton"] > button.nav-btn {
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
    cursor: pointer !important;
}

/* Hover effect */
div[data-testid="stButton"] > button.nav-btn:hover {
    transform: scale(1.08) !important;
    box-shadow: 0 0 45px #00BFFF, 0 0 100px #007BFF !important;
}

/* Back button: deeper blue tone */
div[data-testid="stButton"] > button.nav-btn.back {
    background: linear-gradient(90deg, #007BFF 0%, #0047AB 100%) !important;
}

/* Next button: lighter neon tone */
div[data-testid="stButton"] > button.nav-btn.next {
    background: linear-gradient(90deg, #00BFFF 0%, #1E90FF 100%) !important;
}
</style>
""", unsafe_allow_html=True)

# --- Layout for Back & Next Buttons ---
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)

# Left: Back
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← BACK", key="back-btn", type="secondary"):
        st.switch_page("pages/About.py")

# Right: Next
with col3:
    if st.button("NEXT →", key="next-btn", type="secondary"):
        st.switch_page("pages/More.py")

st.markdown('</div>', unsafe_allow_html=True)