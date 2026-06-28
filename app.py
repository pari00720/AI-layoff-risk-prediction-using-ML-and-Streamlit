import streamlit as st
from pathlib import Path

from components.sidebar import show_sidebar
from components.form import employee_form
from components.dashboard import show_dashboard
from components.analytics import show_analytics
from components.about import show_about

from utils.predictor import predict_employee
from config.constants import APP_TITLE, APP_SUBTITLE


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🤖",
    layout="wide"
)

# ================= LOAD CSS =================
def load_css():
    css_path = Path(__file__).parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

load_css()


# ================= SIDEBAR =================
page = show_sidebar()


# ================= ROUTING =================
if page == "🏠 Prediction":

    st.title(APP_TITLE)
    
    st.markdown(
    f"""
    <p style="
        font-size:36px;
        color:#4B4453;
        line-height:3.6;
        font-weight:800;
    ">
        {APP_SUBTITLE}
    
    """,
    unsafe_allow_html=True
)
    st.divider()

    data = employee_form()

    if data is not None:
        try:
            result = predict_employee(data)
            show_dashboard(result)

        except Exception as e:
            st.error("Prediction failed. Check model or inputs.")
            st.exception(e)


elif page == "📊 Analytics":
    show_analytics()

elif page == "ℹ️ About Project":
    show_about()