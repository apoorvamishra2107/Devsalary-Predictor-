import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# --- 3D Styled Theme ---
st.markdown(
    """
    <style>
    /* Page background */
    .stApp {
        background: linear-gradient(135deg, #f0f2f6 0%, #e0e7ff 100%);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #1E88E5, #42A5F5);
        color: white;
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }

    /* Card-style containers for charts */
    .stContainer {
        background: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Design ---
st.sidebar.markdown(
    """
    <div style="background-color:#1E88E5;padding:20px;border-radius:15px;
                box-shadow: 4px 4px 15px rgba(0,0,0,0.2);margin-bottom:20px;">
        <h2 style="color:white;text-align:center;">💻 Dev Salary Predictor</h2>
        <p style="color:white;text-align:center;font-size:14px;">Explore or Predict Salaries</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Page selection ---
page = st.sidebar.selectbox(
    "Choose Page",
    ("Predict", "Explore")
)

# --- Load selected page ---
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

