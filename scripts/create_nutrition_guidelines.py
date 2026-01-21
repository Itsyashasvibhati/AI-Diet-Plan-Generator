import pandas as pd

data = {
    "disease": ["Diabetes", "Hypertension"],
    "allowed_foods": [
        "Oats, Green vegetables, Nuts",
        "Fruits, Low salt food"
    ],
    "restricted_foods": [
        "Sugar, Junk food",
        "Salt, Fried food"
    ]
}

df = pd.DataFrame(data)
df.to_csv("training/data/nutrition_guidelines.csv", index=False)
print("nutrition_guidelines.csv created")
