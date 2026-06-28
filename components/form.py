import streamlit as st
from config.options import *


def employee_form():

    st.header("👤 Employee Information")
    st.markdown(
    """
    <p style="
        font-size:26px;
        color:#5A525C;
        font-weight:500;
        line-height:2.6;
    ">
    Fill employee details for AI Workforce Risk prediction.
    </p>
    """,
    unsafe_allow_html=True
)

    st.divider()

    # ================= BASIC INFO =================
    st.subheader("📋 Basic Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 70, 25)
        experience = st.number_input("Years of Experience", 0, 50, 2)
        education = st.selectbox("Education Level", EDUCATION_OPTIONS)
        job_level = st.selectbox("Job Level", JOB_LEVEL_OPTIONS)

    with col2:
        industry = st.selectbox("Industry", INDUSTRY_OPTIONS)
        job_role = st.selectbox("Job Role", JOB_ROLE_OPTIONS)
        company_size = st.selectbox("Company Size", COMPANY_SIZE_OPTIONS)
        ai_adoption = st.selectbox("AI Adoption Level", AI_ADOPTION_OPTIONS)

    st.divider()

    # ================= WORK PROFILE =================
    st.subheader("💼 Work Characteristics")

    col1, col2 = st.columns(2)

    with col1:
        routine = st.slider(
            "Routine Task Percentage",
            0, 100, 50,
            help="Higher = more repetitive work"
        )

        creativity = st.slider(
            "Creativity Requirement",
            0, 100, 50,
            help="Higher = less automation risk"
        )

        interaction = st.slider(
            "Human Interaction Level",
            0, 100, 50,
            help="Higher interaction = lower risk"
        )
        training_hours = st.slider(
            "AI Training Hours",
            0, 200, 20
        )

    with col2:
        ai_tools = st.slider(
            "Number of AI Tools Used",
            0, 20, 2
        )

        ai_hours = st.slider(
            "AI Usage Hours / Week",
            0, 80, 10
        )

        tasks_auto = st.slider(
            "Tasks Already Automated (%)",
            0, 100, 20
        )

        

    st.divider()

    # ================= ACTION =================
    st.success("Ready for prediction")

    if st.button("🚀 Analyze Workforce Risk", use_container_width=True):

        return {
            "Age": age,
            "Years_of_Experience": experience,
            "Routine_Task_Percentage": routine,
            "Creativity_Requirement": creativity,
            "Human_Interaction_Level": interaction,
            "Number_of_AI_Tools_Used": ai_tools,
            "AI_Usage_Hours_Per_Week": ai_hours,
            "Tasks_Automated_Percentage": tasks_auto,
            "AI_Training_Hours": training_hours,
            "Education_Level": education,
            "Job_Level": job_level,
            "AI_Adoption_Level": ai_adoption,
            "Industry": industry,
            "Job_Role": job_role,
            "Company_Size": company_size,
        }

    return None