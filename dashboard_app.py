import streamlit as st
st.set_page_config(page_title="Dashboard", layout="wide")
st.title("Dashboard")
st.write("Welcome to the dashboard!")
st.write("This is where you can visualize your data.")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Sample data
data_df = pd.read_csv('kpmi_data-2.csv')
# Display data
st.subheader("Data Overview")
st.dataframe(data_df.head())
# Plotting
st.subheader("Data Visualization")

# --- Safety checks ---
missing = [c for c in ["psychotype", "jobtitle"] if c not in data_df.columns]
if missing:
    st.error(f"Missing columns in data: {missing}")
    st.stop()

import seaborn as sns
import matplotlib.pyplot as plt

# Example: psychotype distribution
fig, ax = plt.subplots(figsize=(10, 6))
data_df["psychotype"].value_counts().plot(kind="bar", ax=ax, color="skyblue")
ax.set_title("Distribution of Psychotypes")
ax.set_xlabel("Psychotype")
ax.set_ylabel("Count")

st.pyplot(fig)  # Display the plot in Streamlit

plt.figure(figsize=(12,6))
sns.countplot(data=data_df, x="psychotype", hue="jobtitle")
plt.xticks(rotation=45)
plt.title("Psychotype counts by Job Title")
plt.show()

cross = pd.crosstab(data_df['jobtitle'], data_df['psychotype'])

plt.figure(figsize=(12,8))
sns.heatmap(cross, cmap="viridis")
plt.title("Job Title vs Psychotype Heatmap")
plt.show()

