from fastapi import APIRouter, UploadFile, File

from app.services.ocr_service import extract_text
from app.services.text_cleaner import clean_text
from app.services.bert_services import predict_disease
from app.services.diet_generator import generate_diet_plan
from app.services.medical_parser import build_medical_intent
from app.services.gpt_service import normalize_rules

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_report(file: UploadFile = File(...)):

    # 1️⃣ OCR - Extract text from medical report
    text = extract_text(await file.read(), file.filename)
    print(f"Extracted text: {text[:200]}...")

    # 2️⃣ Clean text - Preprocess and normalize
    cleaned_text = clean_text(text)
    print(f"Cleaned text: {cleaned_text[:200]}...")

    # 3️⃣ Build medical intent FIRST (extracts biomarkers, patient info)
    medical_intent = build_medical_intent([], cleaned_text)
    print(f"Medical intent: {medical_intent}")
    
    # Get extracted biomarkers for disease prediction
    biomarkers = medical_intent.get("biomarkers", {})

    # 4️⃣ Disease detection (BERT + biomarker-based)
    diseases = predict_disease(cleaned_text, biomarkers)
    print(f"Detected diseases: {diseases}")
    
    # Update medical intent with detected diseases
    medical_intent["conditions"] = diseases

    # 5️⃣ Normalize rules based on conditions and biomarkers
    normalized = normalize_rules(medical_intent)
    print(f"Normalized rules: {normalized}")

    # 6️⃣ Prepare comprehensive GPT output dictionary
    gpt_output = {
        "diet_rules": normalized.get("diet_rules", []),
        "condition": ", ".join(diseases) if diseases else "general wellness",
        "patient": medical_intent.get("patient_info", {}).get("name", "Patient"),
        "medical_condition": diseases if diseases else ["general"],
        "patient_info": medical_intent.get("patient_info", {}),
        "biomarkers": biomarkers,
        "medical_intent": medical_intent,
        "risk_level": medical_intent.get("risk_level", "medium")
    }

    # 7️⃣ Diet generation using LLM (with biomarkers context)
    diet_plan = generate_diet_plan(gpt_output)
    print(f"Generated diet plan successfully")

    return {
        "success": True,
        "detected_conditions": diseases,
        "biomarkers": biomarkers,
        "patient_info": medical_intent.get("patient_info", {}),
        "risk_level": medical_intent.get("risk_level", "medium"),
        "diet_plan": diet_plan
    }
