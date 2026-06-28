import streamlit as st
from config.constants import (
    MODEL_NAME,
    MODEL_DESCRIPTION,
    TECH_STACK,
    DATASET_NAME,
    TARGET_COLUMN,
)


def show_about():

    st.header("ℹ️ About AI Workforce Risk Analyzer")
    st.caption("AI-powered educational project for workforce risk prediction")

    st.divider()

    # ================= OVERVIEW =================
    st.subheader("📌 Project Overview")

    st.write(
        "This project predicts the **AI Layoff Risk** of employees using a Machine Learning model "
        "based on job role, skills, experience, AI usage, and workplace factors."
    )

    st.divider()

    # ================= PROBLEM =================
    st.subheader("🎯 Problem Statement")

    st.write(
        "AI is transforming industries rapidly. Many roles are becoming automated. "
        "This tool helps identify risk levels and suggests skill improvements."
    )

    st.divider()

    # ================= ML MODEL =================
    st.subheader("🧠 Machine Learning Model")

    st.write(f"**Model Used:** {MODEL_NAME}")
    st.write(MODEL_DESCRIPTION)

    st.divider()

    # ================= TECH STACK =================
    st.subheader("🛠 Tech Stack")

    for tech in TECH_STACK:
        st.write("•", tech)

    st.divider()

    # ================= DATASET =================
    st.subheader("📂 Dataset Information")

    st.write(f"**Dataset:** {DATASET_NAME}")
    st.write(f"**Target Column:** {TARGET_COLUMN}")

    st.write(
        """
The dataset includes:
- Job Role
- Education Level
- AI Adoption Level
- Experience
- Automation level
- Creativity & interaction metrics
"""
    )

    st.divider()

    # ================= FEATURES =================
    st.subheader("✨ Key Features")

    st.write(
        """
• AI Layoff Risk Prediction  
• Interactive Dashboard  
• Job Role Recommendations  
• Feature Importance Analysis  
• Educational Career Guidance  
"""
    )

    st.divider()

    # ================= DEVELOPER =================
    st.subheader("👩‍💻 Developer")

    st.success(
        """
Pari Mishra  
B.Tech - AI & ML  
SRMCEM, Lucknow  

Focused on Machine Learning, Data Science & AI Applications
"""
    )

    st.divider()

    st.caption("© 2026 AI Workforce Risk Analyzer")