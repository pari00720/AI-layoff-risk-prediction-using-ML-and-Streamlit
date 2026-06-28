import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from utils.load_model import load_model


def show_analytics():

    st.header("📊 Analytics Dashboard")
    st.caption("Explore dataset insights and workforce trends.")
    st.divider()

    # ================= LOAD DATA =================
    DATA_PATH = Path(__file__).parent.parent / "data" / "ai-impact-jobs-layoff-risk-dataset.csv"
    df = pd.read_csv(DATA_PATH)

    model = load_model()

    # ================= STATS =================
    st.subheader("📌 Key Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Employees", len(df))
    col2.metric("Industries", df["Industry"].nunique())
    col3.metric("Job Roles", df["Job_Role"].nunique())

    col4, col5, col6 = st.columns(3)

    col4.metric("Education Levels", df["Education_Level"].nunique())
    col5.metric("AI Adoption Levels", df["AI_Adoption_Level"].nunique())
    col6.metric("Model", "Random Forest")

    st.divider()

    # ================= DATA PREVIEW =================
    st.subheader("🗂 Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.divider()

    # ================= INDUSTRY DISTRIBUTION =================
    st.subheader("🏢 Industry Distribution")

    industry_counts = df["Industry"].value_counts().reset_index()
    industry_counts.columns = ["Industry", "Count"]

    fig1 = px.bar(
        industry_counts,
        x="Count",
        y="Industry",
        orientation="h",
        title="Employees by Industry"
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

    # ================= JOB ROLE =================
    st.subheader("💼 Top Job Roles")

    role_counts = df["Job_Role"].value_counts().head(10).reset_index()
    role_counts.columns = ["Job_Role", "Count"]

    fig2 = px.bar(
        role_counts,
        x="Count",
        y="Job_Role",
        orientation="h",
        title="Top 10 Job Roles"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ================= PIE CHARTS =================
    col1, col2 = st.columns(2)

    with col1:
        fig3 = px.pie(df, names="Education_Level", title="Education Distribution", hole=0.4)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        fig4 = px.pie(df, names="Company_Size", title="Company Size Distribution", hole=0.4)
        st.plotly_chart(fig4, use_container_width=True)

    st.divider()

    # ================= AI ADOPTION =================
    st.subheader("🤖 AI Adoption Levels")

    adoption_counts = df["AI_Adoption_Level"].value_counts().reset_index()
    adoption_counts.columns = ["AI_Adoption_Level", "Count"]

    fig5 = px.bar(adoption_counts, x="AI_Adoption_Level", y="Count")
    st.plotly_chart(fig5, use_container_width=True)

    st.divider()

    # ================= LAYOFF RISK =================
    st.subheader("⚠ Layoff Risk Distribution")

    risk_counts = df["Layoff_Risk"].value_counts().reset_index()
    risk_counts.columns = ["Layoff_Risk", "Count"]

    fig6 = px.bar(risk_counts, x="Layoff_Risk", y="Count")
    st.plotly_chart(fig6, use_container_width=True)

    st.divider()

    # ================= FEATURE IMPORTANCE =================
    st.subheader("🌲 Feature Importance")

    feature_df = pd.DataFrame({
        "Feature": model.feature_names_in_,
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False).head(10)

    fig7 = px.bar(
        feature_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Top Features"
    )

    st.plotly_chart(fig7, use_container_width=True)

    st.divider()

    st.success("Analytics loaded successfully")