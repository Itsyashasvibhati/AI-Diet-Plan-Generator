import pandas as pd
import random

# Create synthetic medical text data for training
data = []

# Diabetes examples
diabetes_texts = [
    "Patient shows elevated blood glucose levels of 180 mg/dl. Diagnosed with Type 2 Diabetes Mellitus. HbA1c is 7.2%.",
    "Blood sugar test results: Fasting glucose 145 mg/dl. Patient has diabetes with poor glycemic control.",
    "Medical report: Glucose level 160 mg/dl, HbA1c 6.8%. Diabetes management required.",
    "Patient with diabetes, current glucose reading 200 mg/dl after meals. Needs dietary intervention.",
    "Diabetic patient with blood sugar 140 mg/dl. Requires low carbohydrate diet plan."
]

# Hypertension examples
hypertension_texts = [
    "Blood pressure reading: 150/95 mmHg. Diagnosed with hypertension. High sodium intake noted.",
    "Patient has hypertension with BP 160/100 mmHg. Requires low salt diet.",
    "Hypertensive patient, blood pressure 145/90 mmHg. DASH diet recommended.",
    "Medical report shows hypertension, BP readings consistently above 140/90. Low sodium foods advised.",
    "Patient with high blood pressure 155/98 mmHg. Needs dietary salt restriction."
]

# Cholesterol examples
cholesterol_texts = [
    "Lipid profile: Total cholesterol 280 mg/dl, LDL 180 mg/dl. High cholesterol levels.",
    "Patient has hypercholesterolemia with cholesterol 260 mg/dl. Requires low fat diet.",
    "Blood test shows elevated cholesterol 275 mg/dl and LDL 175 mg/dl. Cardiovascular risk.",
    "Cholesterol levels high at 290 mg/dl. Patient needs lipid-lowering diet.",
    "Hyperlipidemia with total cholesterol 265 mg/dl. Dietary modification required."
]

# Healthy examples
healthy_texts = [
    "Routine checkup shows normal blood glucose 90 mg/dl, normal BP 120/80 mmHg, normal cholesterol 180 mg/dl.",
    "Patient is healthy with all biomarkers within normal range. No specific dietary restrictions.",
    "Normal medical report: Glucose 85 mg/dl, BP 118/78 mmHg, cholesterol 175 mg/dl.",
    "All vitals normal. Patient maintains healthy lifestyle with balanced diet.",
    "Comprehensive health check: All parameters normal. No medical conditions detected."
]

# Thyroid examples
thyroid_texts = [
    "Thyroid function test: TSH 0.1 mIU/L, T3 and T4 elevated. Hyperthyroidism diagnosed.",
    "Patient has hypothyroidism with TSH 15 mIU/L. Thyroid hormone replacement therapy.",
    "Thyroid profile shows TSH 12 mIU/L, indicating hypothyroidism. Dietary adjustments needed.",
    "Hyperthyroid patient with TSH 0.05 mIU/L. Increased metabolism requires higher calorie intake.",
    "Thyroid disorder with abnormal TSH levels. Nutritional support for thyroid health."
]

# Add to data
for text in diabetes_texts:
    data.append({"text": text, "label": "diabetes"})

for text in hypertension_texts:
    data.append({"text": text, "label": "hypertension"})

for text in cholesterol_texts:
    data.append({"text": text, "label": "cholesterol"})

for text in healthy_texts:
    data.append({"text": text, "label": "healthy"})

for text in thyroid_texts:
    data.append({"text": text, "label": "thyroid"})

# Shuffle data
random.shuffle(data)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("training/data/medical_text_processed.csv", index=False)

print(f"Created synthetic training data with {len(data)} samples")
print("Label distribution:")
print(df["label"].value_counts())