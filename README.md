# MBTI Career Quest

An interactive Streamlit dashboard designed for high school students choosing a university major and fresh graduates exploring potential career paths.

The dashboard helps users understand MBTI personality types and explore how they relate to career fields, job titles, and reported job satisfaction. Its interactive visualizations provide ideas about possible study and career directions based on personality-related data.

## Live Demo

[Launch MBTI Career Quest](https://rhea-myat-mbti-career-quest.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rhea-myat-mbti-career-quest.streamlit.app/)


## Project Overview

MBTI Career Quest was developed as part of the ICT305 Data Visualisation project.

Choosing a university major or beginning a career can be challenging, especially for students who are still learning about their interests and working preferences. This dashboard provides an engaging starting point for exploring personality types and career possibilities.

Users can examine the distribution of MBTI types across job fields, compare reported job satisfaction, and explore job titles connected with different personality groups.

The application uses a space-themed interface to make the exploration process approachable and engaging.

## Intended Users

The dashboard is primarily designed for:

- High school students exploring university majors
- University students considering possible career directions
- Fresh graduates beginning their career search
- Anyone interested in MBTI personality types and career data

## Main Features

- Introduction to the 16 MBTI personality types
- Interactive MBTI distribution visualizations
- Career-field filtering
- Job-title exploration
- Job-satisfaction comparisons
- Interactive donut charts, bar charts, and treemaps
- Fictional character examples associated with MBTI types
- Supporting personality and career-development resources
- Multipage Streamlit application
- Custom space-themed user interface

## Dashboard Sections

### MBTI Introduction

Introduces the Myers–Briggs Type Indicator and explains how personality-type information is used within the dashboard.

### Career Exploration

Allows users to explore:

- Overall MBTI type distribution
- Personality types across different job fields
- Average reported job satisfaction by MBTI type
- Relationships between job titles and personality types
- Career patterns within selected professional fields

Users can interact with filters and charts to compare personality and career groups.

### Character Explorer

Presents fictional characters associated with the 16 MBTI personality types. This section provides a more familiar and engaging way to understand the characteristics commonly associated with each type.

### Research and Resources

Provides additional resources related to MBTI, personality frameworks, career development, and the dataset used in the project.

## Technologies

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- HTML
- CSS

## Project Structure

```text
Dashboard/
├── .gitignore
├── requirements.txt
├── README.md
├── Dashboard/
    ├── home_pagev5.py
    ├── utils_ui_pages.py
    ├── pages/
    │   ├── About.py
    │   ├── explore.py
    │   └── More.py
    ├── assets/
    │   ├── background.png
    │   ├── logov3.png
    │   ├── Group Photo.png
    │   └── characters/
    └── data/
        └── cleaned_kpmi_data.csv
├── notebooks/
│   └── exploratory and preprocessing notebooks
└── archive/
    ├── prototypes/
    ├── research/
    ├── assets/
    └── data/
```

The primary Streamlit entry point is:

```text
Dashboard/home_pagev5.py
```

Earlier prototypes and research files are retained in `archive/`, while data-preparation and exploratory notebooks are stored in `notebooks/`. These files are not required to run the main application.

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rhea-myat/Dashboard.git
cd Dashboard
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Open the application directory

```bash
cd Dashboard
```

### 5. Run the application

```bash
python -m streamlit run home_pagev5.py
```

Streamlit will display a local address, usually:

```text
http://localhost:8501
```

Open that address in a web browser if it does not open automatically.

## Data

The dashboard uses a career and personality dataset containing information such as:

- Job title
- Job field
- MBTI personality type
- Personality-scale values
- Reported job satisfaction

The data is used to identify descriptive patterns and produce interactive visualizations. The dashboard does not train a predictive model or guarantee that a particular personality type is suitable for a specific career.

## Interpretation

The visualizations show patterns within the project dataset. They should not be interpreted as proof that personality determines career success or satisfaction.

A career that is common among people with a particular MBTI type may still be suitable for people with other personality types.

## Limitations

- MBTI is only one framework for describing personality.
- Personality types do not determine a person’s abilities or future success.
- The dataset may not represent every country, population, profession, or workplace.
- Reported job satisfaction can be influenced by factors not included in the dataset.
- Relationships shown in the dashboard are descriptive and do not establish causation.
- The dashboard does not replace professional educational or career guidance.

University and career decisions should also consider personal interests, academic strengths, qualifications, values, financial circumstances, opportunities, and professional advice.

## Educational Disclaimer

MBTI Career Quest is an educational data-visualization project. It is intended to inspire exploration and discussion rather than provide psychological assessment or definitive career recommendations.

Users should treat the results as a starting point for further research and self-reflection.
