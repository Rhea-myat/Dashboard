import pandas as pd
import matplotlib.pyplot as plt
from utils_ui import load_theme, inject_css_bg, render_box
import streamlit as st
import ipywidgets as widgets # Importing the ipywidgets library with an alias 'widgets'
from IPython.display import display # Importing the display function from IPython.display
from ipywidgets import widgets
from ipywidgets import interact


load_theme()
df = pd.read_csv("cleaned_kpmi_data.csv")
df.isnull().sum()
print()
df.info()
print()
df.jobtitle.unique()
print()
job_field = df['jobfield'].value_counts()
print(job_field)
print()
df.psychotype.unique()  
print()

#Testing data frame x and y for the plotly
X_Part = df["psychotype"]
Y_Part = df["jobtitle"]
JBTitle = df[df['jobtitle'] == 'HR manager']
psychotype_counts = df["psychotype"].value_counts().reset_index()
psychotype_counts.columns = ['Psychotype', 'Count'] 

#streamlit UI
container_a = st.container()
container_b = st.container()
col1, col2, col3, coll3434 = st.columns(4)
# Initialize the state variable
if "show_content" not in st.session_state:
    st.session_state.show_content = False

def bordered_container(content):
    st.markdown(f"""
        <div style="
            border: 2px solid #4A90E2;
            border-radius: 10px;
            padding: 15px;
            background-color: #f8f9fa;
        ">
            {content}
        </div>
    """, unsafe_allow_html=True)
    
#Buttons
with col1:
        if st.button("Home", use_container_width=True):
            st.info("Home")

with col2:
        if st.button("Explore", use_container_width=True):
            st.info("Explore")

with col3:
        if st.button("Data", use_container_width=True):
            st.info("Data")
            
with coll3434:
        if st.button("More", use_container_width=True):
            st.info("More")

#Background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.logo(image='C:\\Users\\NIKO\\Test\\DIGITAL_DYNAMICS_logo.png', size='large')
st.markdown("<br><br>", unsafe_allow_html=True)


#Title
st.markdown("<h1 style='text-align: center;'>Career Data Quest</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

#list one
st.markdown("<p style='text-align:center;'>ANALYSTS</p>",unsafe_allow_html=True)
bt1, bt2, bt3, bt4 = st.columns(4)

with bt1:
    if st.button("INTJ",use_container_width=True ):
        st.session_state.show_content = "A"
with bt2:
    if st.button("INTP",use_container_width=True ):
        st.session_state.show_content = "B"
with bt3:
    if st.button("ENTJ",use_container_width=True ):
        st.session_state.show_content = "C"
with bt4:
    if st.button("ENTP",use_container_width=True ):
        st.session_state.show_content = "D"
        
#Plotly diagram
import plotly.express as px
#TreeMap
# --- FUNCTION ---
def render_treemap_widget(df):
    """
    Creates a treemap visualization with an external dropdown (right side).
    Call this inside any Streamlit container or render_box.
    """
    # Clean data
    df_clean = df[["jobfield", "psychotype", "satisfied"]].dropna(subset=["jobfield", "psychotype", "satisfied"])
    jobfields = sorted(df_clean["jobfield"].unique())

    # Create list for all figures
    figures = []

    # Create individual treemap for each jobfield
    for jobfield in jobfields:
        df_filtered = df_clean[df_clean["jobfield"] == jobfield]

        agg = (df_filtered
               .groupby(["jobfield", "psychotype"], as_index=False)
               .agg(Count=("satisfied", "size"), Satisfaction=("satisfied", "mean")))

        fig = px.treemap(
            agg,
            path=["jobfield", "psychotype"],
            values="Count",
            color="Satisfaction",
            color_continuous_scale="RdYlGn",
            range_color=(0, 1),
            hover_data={
                "jobfield": False,
                "psychotype": False,
                "Count": ":,",
                "Satisfaction": ":.2f"
            }
        )
        fig.update_traces(
            hovertemplate='<b>Psychotype:</b> %{label}<br>'
                          '<b>Count:</b> %{value}<br>'
                          '<b>Satisfaction:</b> %{color:.2f}<extra></extra>'
        )
        fig.update_layout(title=f"{jobfield} Treemap and Satisfaction")
        figures.append(fig)

    # Create overall treemap (All Jobfields)
    agg_all = (df_clean
               .groupby(["jobfield", "psychotype"], as_index=False)
               .agg(Count=("satisfied", "size"), Satisfaction=("satisfied", "mean")))

    tree = px.treemap(
        agg_all,
        path=["jobfield", "psychotype"],
        values="Count",
        color="Satisfaction",
        color_continuous_scale="RdYlGn",
        range_color=(0, 1),
        hover_data={
            "jobfield": False,
            "psychotype": False,
            "Count": ":,",
            "Satisfaction": ":.2f"
        }
    )

    tree.update_traces(
        hovertemplate='<b>Psychotype:</b> %{label}<br>'
                      '<b>Count:</b> %{value}<br>'
                      '<b>Satisfaction:</b> %{color:.2f}<extra></extra>'
    )
    tree.update_layout(title="All Jobfields Treemap and Satisfaction")

    # Layout: treemap (left) + dropdown (right)
    col1, col2 = st.columns([3, 1])

    with col2:
        selected_field = st.selectbox("Select Jobfield:", ["All Jobfields"] + jobfields)

    with col1:
        if selected_field == "All Jobfields":
            st.plotly_chart(tree, use_container_width=True)
        else:
            idx = jobfields.index(selected_field)
            st.plotly_chart(figures[idx], use_container_width=True)

#First container
def first_section():
    st.markdown("<p style='font-type: bold;'><h2>1. YOUR PROFILE</h2></p>", unsafe_allow_html=True)
    render_box(body="<p>This is the left content</p>", markdown=False, variant="white", align="left")
    render_box(body="<p>This is the right content</p>", markdown=False, variant="white", align="right")    

#Donut Chart
def mbti_pie_data(df, type_col='psychotype'):
    counts = df[type_col].value_counts(dropna=False).reset_index()
    counts.columns = [type_col, 'Count']
    return counts.sort_values(by='Count', ascending=False)

# --- Function that builds the MBTI Pie Section ---
def show_mbti_pie(df):
    # Dropdown for job fields
    jobfields = ["All"] + sorted(df["jobfield"].dropna().unique().tolist())
    jobfield = st.selectbox("Select Job Field", jobfields, index=0)

    # Checkbox to toggle label mode
    show_counts = st.checkbox("Show counts in labels", value=True)

    # Filter data
    d = df if jobfield == "All" else df[df["jobfield"] == jobfield]
    data = mbti_pie_data(d, type_col="psychotype")

    # Label mode
    textinfo = "percent+label+value" if show_counts else "percent+label"

    # Pie chart
    fig = px.pie(
        data,
        names="psychotype",
        values="Count",
        hole=0.3,
        hover_data={
            "psychotype": False,
            "Count": ":,",
        }
    )

    fig.update_traces(
        hovertemplate='<b>Psychotype:</b> %{label}<br>' +
                      '<b>Count:</b> %{value}<br>',
        textinfo=textinfo,
        pull=[0.05]*len(data)
    )

    fig.update_layout(
        legend_title_text="MBTI Type",
        title_x=0.5,
        title_font=dict(size=18)
    )

    st.plotly_chart(fig, use_container_width=True)


#Bar chart

# Aggregate data
agg_all = (
    df.groupby(["jobfield", "psychotype"], as_index=False)
      .agg(Count=("satisfied", "size"), Satisfaction=("satisfied", "mean"))
)

# Function for dropdown (right side)
def jobfield_dropdown(df):
    jobfields = ["All Jobfields"] + sorted(df["jobfield"].unique().tolist())
    selected_job = st.selectbox("Select Jobfield", jobfields, index=0)
    return selected_job

# Function for bar chart (left side)
def job_satisfaction_bar(df, jobfield):
    if jobfield == "All Jobfields":
        filtered = (
            df.groupby(["psychotype"], as_index=False)
              .agg(Satisfaction=("Satisfaction", "mean"))
        )
        title = "All Jobfields: Average Satisfaction by Psychotype"
    else:
        filtered = df[df["jobfield"] == jobfield]
        title = f"{jobfield}: Average Satisfaction by Psychotype"

    fig = px.bar(
        filtered,
        x="psychotype",
        y="Satisfaction",
        color="Satisfaction",
        color_continuous_scale="RdYlGn",
        title=title
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title="Satisfaction"),
        title_x=0.5,
        margin=dict(t=60, r=30, l=30, b=40)
    )

    return fig
    

def job_satisfaction_section(df):
    with st.container():
        # Layout: 2 columns (chart left, dropdown right)
        col1, col2 = st.columns([3, 1])

        with col2:
            selected_job = jobfield_dropdown(df)

        with col1:
            fig = job_satisfaction_bar(df, selected_job)
            st.plotly_chart(fig, use_container_width=True)















st.markdown("<br><br>", unsafe_allow_html=True)
#list two
st.markdown("<p style='text-align:center;'>DIPLOMATS (Temporary useless)</p>",unsafe_allow_html=True)
btT1, btT2, btT3, btT4 = st.columns(4)

with btT1:
    if st.button("INFJ",use_container_width=True ):
        st.info("INFJ")
with btT2:
    if st.button("INFP",use_container_width=True ):
        st.info("INFP")
with btT3:
    if st.button("ENFJ",use_container_width=True ):
        st.info("ENTJ")
with btT4:
    if st.button("ENFP",use_container_width=True ):
        st.info("ENTP")
st.markdown("<br><br>", unsafe_allow_html=True)



st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
# Display hidden content when toggled
if st.session_state.show_content == "A":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHAT DRIVES YOU</h3>", unsafe_allow_html=True)
    job_satisfaction_section(agg_all)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHERE YOU THRIVE</h3>", unsafe_allow_html=True)
    show_mbti_pie(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>HOW YOU COMPARE</h3>", unsafe_allow_html=True)
    render_treemap_widget(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

elif st.session_state.show_content == "B":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHAT DRIVES YOU part 2</h3>", unsafe_allow_html=True)
    job_satisfaction_section(agg_all)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHERE YOU THRIVE</h3>", unsafe_allow_html=True)
    show_mbti_pie(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'HOW YOU COMPARE</h3>", unsafe_allow_html=True)
    render_treemap_widget(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

elif st.session_state.show_content == "C":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHAT DRIVES YOU part 3</h3>", unsafe_allow_html=True)
    job_satisfaction_section(agg_all)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHERE YOU THRIVE</h3>", unsafe_allow_html=True)
    show_mbti_pie(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'HOW YOU COMPARE</h3>", unsafe_allow_html=True)
    render_treemap_widget(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

elif st.session_state.show_content == "D":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHAT DRIVES YOU part 4</h3>", unsafe_allow_html=True)
    job_satisfaction_section(agg_all)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>WHERE YOU THRIVE</h3>", unsafe_allow_html=True)
    show_mbti_pie(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>HOW YOU COMPARE</h3>", unsafe_allow_html=True)
    render_treemap_widget(df)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
