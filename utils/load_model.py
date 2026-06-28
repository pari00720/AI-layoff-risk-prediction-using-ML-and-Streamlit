import joblib
from pathlib import Path
MODEL_DIR = Path(__file__).parent.parent / "models"
def load_model():
    model_path = MODEL_DIR / "layoff_risk_model.pkl"
    model = joblib.load(model_path)
    return model
