import joblib
import pandas as pd
from pathlib import Path

from utils.load_model import load_model

# ==========================================================
# Load Model and Preprocessing Objects
# ==========================================================

MODEL_DIR = Path(__file__).parent.parent / "models"

education_encoder = joblib.load(MODEL_DIR / "education_encoder.pkl")
job_encoder = joblib.load(MODEL_DIR / "job_encoder.pkl")
ai_encoder = joblib.load(MODEL_DIR / "ai_encoder.pkl")
ohe = joblib.load(MODEL_DIR / "ohe.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")

model = load_model()

# ==========================================================
# Numerical Features
# ==========================================================

numerical_features = [
    "Age",
    "Years_of_Experience",
    "Routine_Task_Percentage",
    "Creativity_Requirement",
    "Human_Interaction_Level",
    "Number_of_AI_Tools_Used",
    "AI_Usage_Hours_Per_Week",
    "Tasks_Automated_Percentage",
    "AI_Training_Hours",
]

# ==========================================================
# Preprocessing Function
# ==========================================================

def preprocess_input(user_input):

    # Convert dictionary into DataFrame
    input_df = pd.DataFrame([user_input])

    # -------------------------------
    # Ordinal Encoding
    # -------------------------------

    input_df["Education_Level_Encoded"] = education_encoder.transform(
        input_df[["Education_Level"]]
    )

    input_df["Job_Level_Encoded"] = job_encoder.transform(
        input_df[["Job_Level"]]
    )

    input_df["AI_Adoption_Level_Encoded"] = ai_encoder.transform(
        input_df[["AI_Adoption_Level"]]
    )

    # -------------------------------
    # One-Hot Encoding
    # -------------------------------

    nominal_features = [
        "Industry",
        "Job_Role",
        "Company_Size",
    ]

    encoded = ohe.transform(input_df[nominal_features])

    encoded_df = pd.DataFrame(
        encoded,
        columns=ohe.get_feature_names_out(nominal_features),
        index=input_df.index,
    )

    # -------------------------------
    # Remove Original Categorical Columns
    # -------------------------------

    processed_df = pd.concat(
        [
            input_df.drop(
                columns=[
                    "Education_Level",
                    "Job_Level",
                    "AI_Adoption_Level",
                    "Industry",
                    "Job_Role",
                    "Company_Size",
                ]
            ),
            encoded_df,
        ],
        axis=1,
    )

    # -------------------------------
    # Scale Numerical Features
    # -------------------------------

    processed_df[numerical_features] = scaler.transform(
        processed_df[numerical_features]
    )

    # -------------------------------
    # Match Model Feature Order
    # -------------------------------

    final_input = processed_df.reindex(
        columns=model.feature_names_in_,
        fill_value=0,
    )

    return final_input