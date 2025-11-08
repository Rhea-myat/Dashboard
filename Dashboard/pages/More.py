import streamlit as st
from Utils_Module import load_theme, inject_css_bg, render_title, render_box
import base64
from pathlib import Path
from utils_ui_pages import render_side_menu

# Page configuration
st.set_page_config(page_title="More - Space Dashboard", layout="wide")

load_theme()
inject_css_bg("background.png")
render_side_menu("logov3.png")

render_title("FIND OUT MORE", variant="page", align="center", glow=True)
render_title("✨ FIND YOUR FICTIONAL TWIN ✨", variant="section", align="center", glow=True)
render_title("Discover which beloved characters share your MBTI type", variant="description", align="center",
             glow=False)

# Complete character data with all details
# Complete character data with all details
character_details = {
    "INTP": {"file": "Sherlock Holmes.png", "name": "Sherlock Holmes", "source": "Sherlock",
             "traits": ["Analytical", "Logical", "Independent", "Curious"], "nickname": "Analysts",
             "quote": "When you have eliminated the impossible, whatever remains, however improbable, must be the truth.",
             "description": "The quintessential logical problem-solver, prioritizing objective analysis and intellectual exploration above all else."},
    "INTJ": {"file": "Batman.png", "name": "Batman", "source": "DC Comics",
             "traits": ["Strategic", "Determined", "Visionary", "Independent"], "nickname": "Architects",
             "quote": "It's not who I am underneath, but what I do that defines me.",
             "description": "The Dark Knight who uses strategic planning and determination to protect Gotham City."},
    "ENTP": {"file": "Deadpool.png", "name": "Deadpool", "source": "Marvel",
             "traits": ["Innovative", "Witty", "Strategic", "Charismatic"], "nickname": "Debaters",
             "quote": "Hashtag drive-by.",
             "description": "A witty, chaotic debater and unconventional mastermind who constantly generates new ideas and breaks the fourth wall."},
    "ENTJ": {"file": "Darth Vader.png", "name": "Darth Vader", "source": "Star Wars",
             "traits": ["Leadership", "Strategic", "Efficient", "Confident"], "nickname": "Commanders",
             "quote": "I find your lack of faith disturbing.",
             "description": "The commanding Sith Lord who leads with unwavering confidence and strategic prowess."},
    "INFP": {"file": "Spiderman.png", "name": "Spider-Man", "source": "Marvel",
             "traits": ["Empathetic", "Loyal", "Idealistic", "Creative"], "nickname": "Mediators",
             "quote": "With great power comes great responsibility.",
             "description": "The friendly neighborhood hero who balances idealism with a strong sense of responsibility."},
    "INFJ": {"file": "Dumbledore.png", "name": "Dumbledore", "source": "Harry Potter",
             "traits": ["Empathy", "Wisdom", "Idealism", "Integrity"], "nickname": "Advocates",
             "quote": "Happiness can be found even in the darkest of times, if one only remembers to turn on the light.",
             "description": "A visionary, gentle guide who uses profound insight and quiet conviction to lead others toward their greater potential."},
    "ENFP": {"file": "Aang.png", "name": "Aang", "source": "Avatar: The Last Airbender",
             "traits": ["Enthusiastic", "Optimistic", "Creative", "Warm"], "nickname": "Campaigners",
             "quote": "When we hit our lowest point, we are open to the greatest change.",
             "description": "The Avatar who brings hope and balance with infectious enthusiasm and creativity."},
    "ENFJ": {"file": "Wonder Woman.png", "name": "Wonder Woman", "source": "DC Comics",
             "traits": ["Charismatic", "Visionary", "Passionate", "Inspiring"], "nickname": "Protagonists",
             "quote": "It's not about deserve. It's about what you believe. And I believe in love.",
             "description": "The Amazon warrior who inspires others with her vision of a better world."},
    "ISTJ": {"file": "Katniss Everdeen.png", "name": "Katniss Everdeen", "source": "The Hunger Games",
             "traits": ["Logical", "Organised", "Dedicated", "Reliable"], "nickname": "Logisticians",
             "quote": "I volunteer as tribute!",
             "description": "The determined survivor who stands by her principles and protects those she loves."},
    "ISFJ": {"file": "Snow White.png", "name": "Snow White", "source": "Disney",
             "traits": ["Loyal", "Protective", "Dutiful", "Compassionate"], "nickname": "Defenders",
             "quote": "Remember, you're the one who can fill the world with sunshine.",
             "description": "The kind-hearted princess who finds joy in caring for others and spreading kindness."},

}


characters = [
    ("Sherlock Holmes.png", "Sherlock Holmes", "Sherlock", "INTP"),
    ("Batman.png", "Batman", "DC Comics", "INTJ"),
    ("Deadpool.png", "Deadpool", "Marvel", "ENTP"),
    ("Darth Vader.png", "Darth Vader", "Star Wars", "ENTJ"),
    ("Spiderman.png", "Spider-Man", "Marvel", "INFP"),
    ("Dumbledore.png", "Dumbledore", "Harry Potter", "INFJ"),
    ("Aang.png", "Aang", "Avatar: The Last Airbender", "ENFP"),
    ("Wonder Woman.png", "Wonder Woman", "DC Comics", "ENFJ"),
    ("Katniss Everdeen.png", "Katniss Everdeen", "The Hunger Games", "ISTJ"),
    ("Snow White.png", "Snow White", "Disney", "ISFJ"),
    ("Hermione Granger.png", "Hermione Granger", "Harry Potter", "ESTJ"),
    ("Cinderella.png", "Cinderella", "Disney", "ESFJ"),
    ("Indiana Jones.png", "Indiana Jones", "Indiana Jones", "ISTP"),
    ("Harry Potter.png", "Harry Potter", "Harry Potter", "ISFP"),
    ("James Bond.png", "James Bond", "007", "ESTP"),
    ("Paimon.png", "Paimon", "Genshin Impact", "ESFP"),
]

# Initialize session state for modal
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False
    st.session_state.selected_char = None

# Check for URL parameters (for modal trigger)
query_params = st.query_params
if 'char' in query_params:
    st.session_state.show_modal = True
    st.session_state.selected_char = query_params['char']
    st.query_params.clear()

# CSS
st.markdown("""
<style>
.character-box {
    --accent:#00BFFF;
    --bg:rgba(10,15,30,.55);
    --border:rgba(0,191,255,.35);
    --glow:0 0 18px rgba(0,191,255,.45);
    width:100%;
    border-radius:18px;
    padding:1.5rem 1rem;
    border:1px solid var(--border);
    background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)), var(--bg);
    backdrop-filter: blur(6px);
    box-shadow: var(--glow);
    position:relative;
    overflow:hidden;
    transition: all 0.3s ease;
    text-align: center;
    min-height: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.character-box:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(0,191,255,.65);
}

.character-box.frame{
    background: rgba(12,18,34,.6);
    border:2px solid var(--border);
    box-shadow: 0 0 0 2px rgba(255,255,255,.04) inset, var(--glow);
    padding:1.5rem 1rem;
    border-radius:22px;
}

.character-box:before, .character-box:after{
    content:"";
    position:absolute;
    width:25px; 
    height:6px; 
    border:1px solid var(--border);
    opacity:.6;
}

.character-box:before {
    bottom: 10px;
    right: 10px;
    border-top:none; 
    border-left:none;
    border-radius:0 0 5px 0;
}

.character-box:after{ 
    top: 10px;
    left: 10px;
    border-bottom:none; 
    border-right:none;
    border-radius:5px 0 0 0;
}

.character-image {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid rgba(0,191,255,.4);
    box-shadow: 0 0 12px rgba(0,191,255,.3);
    margin-bottom: 1rem;
}

.character-name {
    font-size: 1rem;
    font-weight: 700;
    color: #E6F3FF;
    margin: 0.5rem 0 0.3rem 0;
    letter-spacing: 0.05em;
    line-height: 1.2;
}

.character-source {
    font-size: 0.8rem;
    color: #E6F3FF;
    opacity: 0.7;
    margin: 0.2rem 0 0.6rem 0;
}

.character-mbti {
    display: inline-block;
    background: linear-gradient(135deg, rgba(138,43,226,.3), rgba(75,0,130,.3));
    border: 2px solid rgba(138,43,226,.6);
    color: #E6F3FF;
    padding: 0.5rem 1.1rem;
    border-radius: 18px;
    font-size: 0.9rem;
    font-weight: 900;
    letter-spacing: 0.1em;
    margin-top: 0.3rem;
    text-shadow: 0 0 8px rgba(138,43,226,.8);
}
</style>
""", unsafe_allow_html=True)

# Render character grid with click handlers using HTML links
for row in range(4):
    col1, col2, col3, col4 = st.columns(4)
    for idx, col in enumerate([col1, col2, col3, col4]):
        char_idx = row * 4 + idx
        img_file, name, source, mbti = characters[char_idx]

        with col:
            # Load image
            try:
                img_path = Path(img_file)
                if img_path.exists():
                    with open(img_path, "rb") as f:
                        img_data = base64.b64encode(f.read()).decode()
                    ext = img_path.suffix.lower()
                    mime_type = "image/jpeg" if ext in ['.jpg', '.jpeg'] else "image/png"
                    img_html = f'<img src="data:{mime_type};base64,{img_data}" class="character-image" alt="{name}">'
                else:
                    img_html = '<div style="width:110px;height:110px;border-radius:50%;background:#445;border:3px solid rgba(0,191,255,.4);margin-bottom:1rem;"></div>'
            except:
                img_html = '<div style="width:110px;height:110px;border-radius:50%;background:#445;border:3px solid rgba(0,191,255,.4);margin-bottom:1rem;"></div>'

            # Clickable character box using anchor tag with query parameter
            st.markdown(f"""
            <a href="?char={mbti}" style="text-decoration: none;">
                <div class="character-box frame">
                    {img_html}
                    <div class="character-name">{name}</div>
                    <div class="character-source">{source}</div>
                    <div class="character-mbti">{mbti}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

# Show modal dialog if character selected
if st.session_state.show_modal and st.session_state.selected_char:
    char_detail = character_details[st.session_state.selected_char]


    @st.dialog(char_detail['name'])
    def show_character_modal():
        # Load image
        try:
            img_path = Path(char_detail['file'])
            if img_path.exists():
                st.image(str(img_path), width=200)
        except:
            pass

        st.markdown(f"### {char_detail['source']}")
        st.markdown(f"## {st.session_state.selected_char} - {char_detail['nickname']}")

        st.markdown("#### Key Traits")
        cols = st.columns(2)
        for idx, trait in enumerate(char_detail['traits']):
            cols[idx % 2].markdown(f"✨ **{trait}**")

        st.markdown("#### Iconic Quote")
        st.info(f'"{char_detail["quote"]}"')

        st.markdown("#### Character Description")
        st.write(char_detail['description'])

        if st.button("Close", use_container_width=True):
            st.session_state.show_modal = False
            st.session_state.selected_char = None
            st.rerun()


    show_character_modal()

st.markdown("<br><br>", unsafe_allow_html=True)

# Rest of your More.py (resources, team photo, footer)
render_title("📚 ACADEMIC RESOURCES 📚", variant="section", align="center", glow=True)
render_title("Explore the research behind personality typing and career psychology", variant="description",
             align="center", glow=False)

resources = [
    ("📄 Primary Source", "MBTI Manual: A Guide to the Development and Use of the Myers-Briggs Type Indicator",
     "Myers, I. B., McCaulley, M. H., Quenk, N. L., & Hammer, A. L. (1998)", "Consulting Psychologists Press",
     "The comprehensive guide to understanding and applying MBTI in career and personal development contexts.",
     "https://asia.themyersbriggs.com/"),
    ("📊 Dataset", "Kaggle MBTI Career Dataset", "pmenshih (2024)", "Kaggle Datasets",
     "The primary dataset used in this dashboard, containing MBTI type distributions and career satisfaction ratings.",
     "https://www.kaggle.com/datasets/pmenshih/kpmi-mbti-mod-test"),
    ("🌐 Online Resource", "16Personalities - Free Personality Test", "NERIS Analytics Limited (2024)",
     "16Personalities.com", "Modern adaptation of personality typing with comprehensive career insights and resources.",
     "https://www.16personalities.com/"),
    ("📘 Academic", "Guide Do What You Are - Personality Type Handbook", "Andrews University (n.d.)",
     "Andrews University Career Services",
     "A comprehensive handbook guide to understanding personality types and their career implications.",
     "https://www.andrews.edu/services/career_services/documents/dwya.pdf"),
    ("🌐 Online Resource", "The Official Source (Myers-Briggs Foundation)", "Myers-Briggs Foundation (2024)",
     "The Myers & Briggs Foundation",
     "Official resource connecting personality type to career paths and professional development.",
     "https://www.myersbriggs.org/type-in-my-life/personality-type-and-careers/"),
]

st.markdown("""
<style>
.resource-box {
    --accent:#9F7AEA;
    --bg:rgba(10,15,30,.55);
    --border:rgba(159,122,234,.35);
    --glow:0 0 18px rgba(159,122,234,.45);
    width:100%;
    max-width: 1180px;
    margin: 2rem auto;
    border-radius:18px;
    padding:2rem 2.5rem;
    border:1px solid var(--border);
    background: linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01)), var(--bg);
    backdrop-filter: blur(6px);
    box-shadow: var(--glow);
    position:relative;
    overflow:hidden;
}
.resource-box.frame{
    background: rgba(12,18,34,.6);
    border:2px solid var(--border);
    box-shadow: 0 0 0 2px rgba(255,255,255,.04) inset, var(--glow);
    padding:2rem 2.5rem;
    border-radius:22px;
}
.resource-box:before, .resource-box:after{
    content:"";
    position:absolute;
    width:42px; 
    height:10px; 
    border:1px solid var(--border);
    opacity:.6;
}
.resource-box:before {
    bottom: 18px;
    right: 18px;
    border-top:none; 
    border-left:none;
    border-radius:0 0 8px 0;
}
.resource-box:after{ 
    top: 18px;
    left: 18px;
    border-bottom:none; 
    border-right:none;
    border-radius:8px 0 0 0;
}
.resource-badge {
    display: inline-block;
    background: rgba(159,122,234,.2);
    border: 1px solid rgba(159,122,234,.4);
    color: #E6F3FF;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    margin-bottom: 1rem;
}
.resource-title {
    font-size: 1.8rem;
    font-weight: 900;
    color: #E6F3FF;
    margin-bottom: 1rem;
    letter-spacing: 0.05em;
    line-height: 1.3;
}
.resource-citation {
    font-size: 1.1rem;
    color: #E6F3FF;
    margin: 0.5rem 0;
    font-style: italic;
    opacity: 0.9;
}
.resource-publisher {
    font-size: 1.1rem;
    color: #E6F3FF;
    margin: 0.3rem 0;
    opacity: 0.85;
}
.resource-description {
    font-size: 1rem;
    color: #E6F3FF;
    line-height: 1.6;
    margin-top: 1rem;
    opacity: 0.8;
}
.view-button {
    display: inline-block;
    background: rgba(159,122,234,.3);
    border: 2px solid rgba(159,122,234,.6);
    color: #E6F3FF;
    padding: 0.7rem 1.5rem;
    border-radius: 10px;
    font-size: 1rem;
    font-weight: 700;
    text-decoration: none;
    letter-spacing: 0.08em;
    transition: all 0.3s ease;
    text-transform: uppercase;
}
.view-button:hover {
    background: rgba(159,122,234,.5);
    border-color: rgba(159,122,234,.9);
    box-shadow: 0 0 15px rgba(159,122,234,.6);
    transform: translateY(-2px);
    color: #E6F3FF;
    text-decoration: none;
}
.view-button::after {
    content: " ↗";
    margin-left: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

for badge, title, citation, publisher, description, url in resources:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="resource-box frame">
            <div><span class="resource-badge">{badge}</span></div>
            <h3 class="resource-title">{title}</h3>
            <p class="resource-citation">{citation}</p>
            <p class="resource-publisher">{publisher}</p>
            <p class="resource-description">{description}</p>
            <br>
            <a href="{url}" target="_blank" class="view-button">View</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

render_title("👥 MEET OUR TEAM 👥", variant="section", align="center", glow=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Group Photo.png", use_container_width=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown("""
<style>
.footer-container {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem 0;
    margin-top: 4rem;
}
.footer-link {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.3rem;
    font-weight: 900;
    color: #E6F3FF;
    text-decoration: none;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 1rem 2rem;
    background: rgba(10, 15, 30, 0.8);
    border: 2px solid rgba(0, 191, 255, 0.4);
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0, 191, 255, 0.4);
    backdrop-filter: blur(10px);
    transition: all 0.3s ease;
    cursor: pointer;
    display: inline-block;
}
.footer-link:hover {
    color: #00FFFF;
    border-color: rgba(0, 191, 255, 0.8);
    box-shadow: 0 0 30px rgba(0, 191, 255, 0.7);
    transform: translateY(-3px);
    text-decoration: none;
}
</style>
<div class="footer-container">
    <a href="https://docs.google.com/forms/d/e/1FAIpQLScWs-_zQ8fZ2FUh8cuZpLF3X_DkJPjPvGZIXbxc46C7NEwlZw/viewform?usp=publish-editor" 
       target="_blank" 
       class="footer-link">
        📝 Feedback Form
    </a>
</div>
""", unsafe_allow_html=True)

import streamlit as st

# --- Back & Next Button Styles ---
st.markdown("""
<style>
.nav-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    margin-top: 3rem;
    padding: 0 6rem; /* adjust spacing from page edges */
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

/* Back button: deeper tone */
div[data-testid="stButton"] > button.nav-btn.back {
    background: linear-gradient(90deg, #007BFF 0%, #0047AB 100%) !important;
}

/* Next button: lighter tone */
div[data-testid="stButton"] > button.nav-btn.next {
    background: linear-gradient(90deg, #00BFFF 0%, #1E90FF 100%) !important;
}
</style>
""", unsafe_allow_html=True)

# --- Layout for Back & Next Buttons ---
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)

# Left: Back (to Explore)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← BACK", key="back-btn", type="secondary"):
        st.switch_page("pages/explore.py")


st.markdown('</div>', unsafe_allow_html=True)