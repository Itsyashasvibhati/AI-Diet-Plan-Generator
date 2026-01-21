from backend.app.services.ocr_service import extract_text
from backend.app.services.text_cleaner import clean_text
from pathlib import Path
import pandas as pd

pdf_files = [
    "data/raw/prescriptions/Medicalreport.pdf",
    "data/raw/prescriptions/scannedImages.pdf"
]

rows = []

for pdf in pdf_files:
    with open(pdf, "rb") as f:
        raw_text = extract_text(f.read(), pdf)

    cleaned = clean_text(raw_text)

    rows.append({
        "text": cleaned,
        "label": "unknown"  # will be predicted by model
    })

df = pd.DataFrame(rows)
df.to_csv("training/data/medical_text.csv", index=False)

print("✅ medical_text.csv created from PDFs")
