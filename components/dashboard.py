import streamlit as st
from config.constants import RISK_DESCRIPTION
from config.recommendations import ROLE_RECOMMENDATIONS


def show_dashboard(result):

    pred = result["prediction"]
    conf = result["confidence"]
    probs = result["probabilities"]
    data = result["employee_data"]
    role = result["job_role"]

    st.header("📊 Prediction Dashboard")
    st.divider()

    # ================= RISK STATUS =================
    if pred == 0:
        st.success("🟢 LOW RISK — Stable Career Outlook")
    elif pred == 1:
        st.warning("🟡 MEDIUM RISK — Upskilling Recommended")
    else:
        st.error("🔴 HIGH RISK — Immediate Action Required")

    # ================= METRICS =================
    col1, col2, col3 = st.columns(3)

    col1.metric("Prediction", ["Low", "Medium", "High"][pred])
    col2.metric("Confidence", f"{conf * 100:.2f}%")
    col3.metric("Job Role", role)

    st.divider()

    # ================= PROBABILITY =================
    st.subheader("📈 Risk Probability")

    st.write("Low Risk")
    st.progress(float(probs["Low Risk"]))

    st.write("Medium Risk")
    st.progress(float(probs["Medium Risk"]))

    st.write("High Risk")
    st.progress(float(probs["High Risk"]))

    st.divider()

    # ================= INTERPRETATION =================
    st.subheader("📖 Explanation")
    st.write(RISK_DESCRIPTION[pred])

    st.divider()

    # ================= CAREER RECOMMENDATIONS (FIXED) =================
    st.subheader("🤖 Career Guidance")

    rec = ROLE_RECOMMENDATIONS.get(role)

    if rec:

        level_data = rec.get("high") or rec.get("medium")

        if level_data:

            st.markdown("### 🧠 Recommended Skills")
            for skill in level_data.get("skills", []):
                st.write("•", skill)

            if level_data.get("certifications"):
                st.markdown("### 🎓 Certifications")
                for cert in level_data.get("certifications", []):
                    st.write("•", cert)

    else:
        st.info("No specific recommendations available for this role.")

    st.divider()

    # ================= KEY INSIGHTS =================
    st.subheader("📌 Key Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Role:**", role)
        st.write("**Experience:**", data["Years_of_Experience"])
        st.write("**AI Adoption:**", data["AI_Adoption_Level"])
        st.write("**Education:**", data["Education_Level"])

    with col2:
        st.write("**AI Tools Used:**", data["Number_of_AI_Tools_Used"])
        st.write("**AI Usage (hrs/week):**", data["AI_Usage_Hours_Per_Week"])
        st.write("**Training Hours:**", data["AI_Training_Hours"])

    st.divider()

    # ================= DISCLAIMER =================
    st.warning(
        "This is an educational ML project and not a real-world hiring or layoff decision system."
    )