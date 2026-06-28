# ==========================================================
# Application
# ==========================================================

APP_TITLE = "🤖 AI Workforce Risk Analyzer"

APP_SUBTITLE = """
Predict an employee's Layoff Risk due to adoption of AI Tools using Machine Learning.
"""

# ==========================================================
# Risk Labels
# ==========================================================

RISK_LABELS = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk",
}

# ==========================================================
# Risk Descriptions
# ==========================================================

RISK_DESCRIPTION = {
    0: """
The employee currently has a **Low AI Layoff Risk**.

The role involves significant human interaction,
creativity or decision-making, making it relatively
less susceptible to automation.

Continue learning modern AI tools to remain competitive.
""",
    1: """
The employee has a **Medium AI Layoff Risk**.

Some responsibilities may become automated over time.

Improving AI knowledge, analytical thinking and
industry-specific skills can reduce future risk.
""",
    2: """
The employee has a **High AI Layoff Risk**.

The role contains a high proportion of repetitive
tasks and may be significantly impacted by AI-driven
automation.

Immediate upskilling in AI-assisted technologies,
problem solving and advanced technical skills is
strongly recommended.
""",
}

# ==========================================================
# Certifications
# ==========================================================

CERTIFICATIONS = [
    "Google AI Essentials",
    "Microsoft AI-900: Azure AI Fundamentals",
    "IBM AI Engineering Professional Certificate",
    "AWS Certified Cloud Practitioner",
    "Google Data Analytics Professional Certificate",
]

# ==========================================================
# Technologies
# ==========================================================

TECH_STACK = [
    "Python",
    "Pandas",
    "NumPy",
    "Scikit-Learn",
    "Streamlit",
    "Plotly",
    "Joblib",
]

# ==========================================================
# Model Information
# ==========================================================

MODEL_NAME = "Random Forest Classifier"

MODEL_DESCRIPTION = """
Random Forest is an ensemble machine learning algorithm
that combines multiple decision trees to improve
prediction accuracy while reducing overfitting.
"""

# ==========================================================
# Dataset Information
# ==========================================================

DATASET_NAME = "AI Workforce Risk Dataset"

TARGET_COLUMN = "Layoff_Risk"

TARGET_CLASSES = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk",
}

# ==========================================================
# Footer
# ==========================================================

FOOTER = """
© 2026 AI Workforce Risk Analyzer

Developed by Pari Mishra
"""