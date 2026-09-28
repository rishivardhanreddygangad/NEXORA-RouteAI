import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# ==========================================
# SKRYPTORA - AI RISK PREDICTION MODEL
# ==========================================

data = {
    "rainfall": [0, 20, 40, 70, 90, 10, 60, 85, 30, 75, 15, 95],
    "road_condition": [1, 1, 2, 3, 3, 1, 2, 3, 2, 3, 1, 3],
    "landslide_risk": [0, 0, 10, 30, 70, 0, 20, 80, 10, 60, 0, 90],
    "flood_risk": [0, 5, 10, 40, 80, 0, 30, 70, 15, 50, 5, 90],
    "connectivity": [90, 85, 70, 50, 30, 95, 60, 35, 75, 45, 90, 20],
    "cargo_priority": [1, 2, 2, 3, 3, 1, 2, 3, 1, 3, 2, 3],
    "risk": [
        0, 0, 1, 1, 2, 0,
        1, 2, 0, 2, 0, 2
    ]
}

df = pd.DataFrame(data)

X = df.drop("risk", axis=1)
y = df["risk"]

# ==========================================
# TRAIN MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, "risk_model.pkl")

print("===================================")
print("SKRYPTORA AI MODEL TRAINED")
print("===================================")
print("Model: Random Forest Classifier")
print("Classes:")
print("0 = LOW")
print("1 = MEDIUM")
print("2 = HIGH")
print("===================================")
print("Saved as: risk_model.pkl")