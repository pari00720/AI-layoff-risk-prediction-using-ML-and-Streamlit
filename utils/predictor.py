from utils.load_model import load_model
from utils.preprocess import preprocess_input

# ==========================================================
# Load Model Once
# ==========================================================

model = load_model()

# ==========================================================
# Prediction Function
# ==========================================================

def predict_employee(employee_data):
    """
    Predict an employee's layoff risk due to impact of AI tools.
    """

    # Preprocess input
    processed_data = preprocess_input(employee_data)

    # Prediction
    prediction = int(model.predict(processed_data)[0])

    # Prediction probabilities
    probability = model.predict_proba(processed_data)[0]

    # Risk labels
    risk_labels = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk",
    }

    # Return result
    result = {
        "prediction": prediction,
        "risk_level": risk_labels[prediction],
        "confidence": float(probability[prediction]),
        "probabilities": {
            "Low Risk": float(probability[0]),
            "Medium Risk": float(probability[1]),
            "High Risk": float(probability[2]),
        },
        "employee_data":employee_data,
        # ======================================================
        # Information required for personalized recommendations
        # ======================================================
        "job_role": employee_data["Job_Role"],
    }

    return result