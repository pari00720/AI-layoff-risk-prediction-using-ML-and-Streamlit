import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🤖 AI Workforce Risk")

        st.caption("ML-powered career risk analyzer")

        st.divider()

        # ================= NAVIGATION =================
        page = st.radio(
            "Navigation",
            ["🏠 Prediction", "📊 Analytics", "ℹ️ About Project"]
        )

        st.divider()

        # ================= ABOUT =================
        st.subheader("📌 About")

        st.write(
            """
This app predicts AI-based job risk using a Random Forest model.

It analyzes:
• Job role  
• AI adoption  
• Experience  
• Work patterns  
"""
        )

        st.divider()

        # ================= DEVELOPER =================
        st.subheader("👩‍💻 Developer")

        st.write("Pari Mishra")
        st.caption("B.Tech AI & ML")
        st.caption("SRMCEM, Lucknow")

        st.divider()

        st.caption("Version 1.0")

    return page