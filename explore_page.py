import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ Data Cleaning Functions ------------------
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

# ------------------ Load Data ------------------
@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df[df["ConvertedComp"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 10000]
    df = df[df["Country"] != "Other"]
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

# ------------------ Explore Page ------------------
def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    # ------------------ Prepare data ------------------
    data_country = df["Country"].value_counts()
    data_bar = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    data_line = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)

    # ------------------ PIE CHART ------------------
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(8,8))
    ax1.pie(
        data_country,
        labels=None,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        textprops={'fontsize': 8}
    )
    ax1.axis("equal")
    ax1.legend(
        data_country.index,
        title="Countries",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )
    st.write("#### Number of Data from Different Countries")
    st.pyplot(fig1)
    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ BAR CHART (full width) ------------------
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)
    st.write("#### Mean Salary by Country")
    st.bar_chart(data_bar, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ------------------ LINE CHART (full width) ------------------
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)
    st.write("#### Mean Salary by Experience")
    st.line_chart(data_line, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

