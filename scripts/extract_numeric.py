import pandas as pd

df = pd.read_csv("data/raw/diabetes_012_health_indicators_BRFSS2015.csv")

selected = df[[
    "BMI",
    "Age",
    "HighBP",
    "HighChol",
    "PhysActivity",
    "GenHlth",
    "Diabetes_012"
]]

selected.fillna(0, inplace=True)

selected.to_csv("training/data/medical_numeric.csv", index=False)
print("✅ medical_numeric.csv created")
