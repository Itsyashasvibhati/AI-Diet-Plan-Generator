#!/usr/bin/env python3
"""
Test script for AI-NutriCare improvements
Tests biomarker extraction, disease detection, and diet rule generation
"""

def test_biomarker_extraction():
    """Test biomarker extraction from medical report text"""
    print("\n" + "="*60)
    print("Testing Biomarker Extraction")
    print("="*60 + "\n")
    
    # Sample medical report text
    sample_text = """
    Department of Biochemistry
    Patient: Chanda Devi, Age: 50, Female
    
    Investigation Results:
    CK MB: 28 U/L (Reference: <24)
    Fasting Glucose: 145 mg/dl (Reference: 70-100)
    TSH: 3.5 mIU/L (Reference: 0.4-4.0)
    Total Cholesterol: 245 mg/dl (Reference: <200)
    HDL: 35 mg/dl (Reference: >40)
    LDL: 160 mg/dl (Reference: <100)
    Triglycerides: 180 mg/dl (Reference: <150)
    Blood Pressure: 150/95 mmHg
    """
    
    from backend.app.services.medical_parser import extract_biomarkers
    
    biomarkers = extract_biomarkers(sample_text)
    
    print("✅ Extracted Biomarkers:")
    for marker, data in biomarkers.items():
        value = data.get("value", "N/A")
        unit = data.get("unit", "")
        abnormal = data.get("abnormal", "N/A")
        print(f"   {marker:20} = {value:8} {unit:10} (Abnormal: {abnormal})")
    
    # Expected biomarkers
    expected = ["ck_mb", "fasting_glucose", "blood_pressure", "total_cholesterol", "hdl", "ldl", "triglycerides"]
    found = [m for m in expected if m in biomarkers]
    
    print(f"\n✅ Found {len(found)}/{len(expected)} key biomarkers")
    return len(found) >= 5

def test_disease_detection():
    """Test disease detection with biomarkers"""
    print("\n" + "="*60)
    print("Testing Disease Detection")
    print("="*60 + "\n")
    
    sample_text = """
    CK MB: 28 U/L - Cardiac marker elevated
    Fasting Glucose: 145 mg/dl - Hyperglycemia
    Blood Pressure: 150/95 - Hypertension
    """
    
    # Mock biomarkers
    biomarkers = {
        "ck_mb": {"value": 28, "abnormal": True},
        "fasting_glucose": {"value": 145, "abnormal": True},
        "blood_pressure": {"value": "150/95", "abnormal": True}
    }
    
    from backend.app.services.bert_services import detect_diseases_from_biomarkers
    
    diseases = detect_diseases_from_biomarkers(biomarkers)
    
    print("✅ Detected Diseases:")
    for disease in diseases:
        print(f"   - {disease}")
    
    expected_diseases = ["diabetes", "hypertension", "heart_disease"]
    found = [d for d in expected_diseases if d in diseases]
    
    print(f"\n✅ Found {len(found)}/{len(expected_diseases)} key diseases")
    return len(found) >= 2

def test_diet_rules_generation():
    """Test diet rule generation"""
    print("\n" + "="*60)
    print("Testing Diet Rules Generation")
    print("="*60 + "\n")
    
    medical_intent = {
        "conditions": ["diabetes", "hypertension", "heart_disease"],
        "biomarkers": {
            "fasting_glucose": {"value": 145, "abnormal": True},
            "blood_pressure": {"value": "150/95", "abnormal": True},
            "ck_mb": {"value": 28, "abnormal": True}
        }
    }
    
    from backend.app.services.gpt_service import normalize_rules
    
    normalized = normalize_rules(medical_intent)
    
    print("✅ Generated Diet Rules:")
    for i, rule in enumerate(normalized["diet_rules"], 1):
        print(f"   {i}. {rule}")
    
    print(f"\n✅ Generated {len(normalized['diet_rules'])} specific diet rules")
    
    # Check for condition-specific rules
    rules_text = " ".join(normalized["diet_rules"]).lower()
    has_diabetes_rules = "glycemic" in rules_text or "carbohydrate" in rules_text
    has_hypertension_rules = "sodium" in rules_text or "dash" in rules_text
    has_cardiac_rules = "omega" in rules_text or "mediterranean" in rules_text
    
    print(f"\n✅ Diabetes-specific rules: {has_diabetes_rules}")
    print(f"✅ Hypertension-specific rules: {has_hypertension_rules}")
    print(f"✅ Cardiac-specific rules: {has_cardiac_rules}")
    
    return has_diabetes_rules and has_hypertension_rules

def test_patient_info_extraction():
    """Test patient information extraction"""
    print("\n" + "="*60)
    print("Testing Patient Info Extraction")
    print("="*60 + "\n")
    
    sample_text = """
    Patient Name: Chanda Devi
    Age/Sex: 50 Yr/F
    DOB: 15-Jan-1974
    Ward: 5th D Female Ward
    """
    
    from backend.app.services.medical_parser import extract_patient_info
    
    patient_info = extract_patient_info(sample_text)
    
    print("✅ Extracted Patient Info:")
    for key, value in patient_info.items():
        print(f"   {key:15} = {value}")
    
    print(f"\n✅ Extracted {len(patient_info)} patient details")
    return len(patient_info) >= 2

def test_openai_import():
    """Test OpenAI v1.0.0+ import"""
    print("\n" + "="*60)
    print("Testing OpenAI API v1.0.0+")
    print("="*60 + "\n")
    
    try:
        from openai import OpenAI
        print("✅ OpenAI client imported successfully")
        print("✅ Using new API (v1.0.0+)")
        return True
    except ImportError as e:
        print(f"❌ Failed to import OpenAI: {e}")
        print("   Run: pip install openai>=1.0.0")
        return False

def main():
    print("\n" + "="*60)
    print("AI-NutriCare - Improvement Test Suite")
    print("="*60)
    
    tests = [
        ("OpenAI API v1.0.0+", test_openai_import),
        ("Biomarker Extraction", test_biomarker_extraction),
        ("Disease Detection", test_disease_detection),
        ("Patient Info Extraction", test_patient_info_extraction),
        ("Diet Rules Generation", test_diet_rules_generation),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"\n❌ Error in {test_name}: {e}")
            import traceback
            traceback.print_exc()
            results[test_name] = False
    
    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60 + "\n")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅" if result else "❌"
        print(f"{status} {test_name}")
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✅ All tests passed! System is ready for deployment.")
    else:
        print(f"\n❌ {total - passed} test(s) failed. Please check the errors above.")
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
