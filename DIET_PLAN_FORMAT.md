# 📋 Systematic Diet Plan Display Format

## 🎯 How the Diet Plan is Organized

The AI-NutriCare system now displays diet plans in a **systematic, easy-to-understand format** with clear sections and visual hierarchy.

## 📅 Day Structure

Each day is displayed with a prominent header:

```
DAY 1
═══════════════
```

## 🍽️ Meal Sections

Meals are clearly separated with icons and colors:

### 🌅 Breakfast

- **Food Item 1** - Portion size and preparation notes
- **Food Item 2** - Specific instructions
- **Beverage** - What to drink

### ☀️ Lunch

- **Main Dish** - Complete meal description
- **Side Dish** - Accompaniments
- **Salad** - Fresh vegetables

### 🌙 Dinner

- **Protein** - Lean protein sources
- **Vegetables** - Steamed or grilled
- **Carbs** - Controlled portions

### 🍪 Snacks (if applicable)

- **Mid-morning** - Healthy snack options
- **Afternoon** - Energy-boosting foods

## 💡 General Guidelines

Important notes and tips are highlighted:

- 💡 **Hydration**: Drink 8-10 glasses of water daily
- 💡 **Portion Control**: Use smaller plates
- 💡 **Meal Timing**: Eat every 3-4 hours

## 🎨 Visual Features

- **Color-coded sections** for different meal types
- **Icons** for easy identification (🌅 breakfast, ☀️ lunch, etc.)
- **Structured layout** with proper spacing
- **Bold formatting** for important items
- **Bullet points** for food lists

## 📝 Example Output Structure

```
DAY 1
🌅 BREAKFAST
• Oatmeal (1/2 cup cooked) with berries
• Greek yogurt (1 cup) plain, low-fat
• Green tea (1 cup) unsweetened

☀️ LUNCH
• Grilled chicken breast (4 oz) skinless
• Mixed green salad (2 cups) with olive oil dressing
• Brown rice (1/2 cup cooked)

🌙 DINNER
• Baked salmon (4 oz) with lemon
• Steamed broccoli (1 cup)
• Sweet potato (1 medium, baked)

🍪 SNACKS
• Apple (1 medium) with 1 tbsp almond butter
• Handful of almonds (10-12 nuts)

💡 GENERAL NOTES
• Maintain consistent meal times
• Drink water between meals
• Monitor blood sugar levels
```

Repository layout (important folders)

- `backend/` : Backend service code (Flask/FastAPI-style routes, services, and models).
- `backend/app/services/ocr_service.py` : OCR helper that extracts text from PDFs/images.
- `backend/app/services/medical_parser.py` : Extracts patient demographics and biomarkers from OCR text.
- `backend/app/services/bert_services.py` : BERT-related model utilities (disease classification).
- `backend/app/services/diet_generator.py` : Rule-based + LLM-backed diet recommendation logic.
- `frontend/` : Minimal UI; contains `frontend/app.py` for displaying results.
- `training/` : Scripts and data used for training or evaluating models.
- `data/raw/` : Raw datasets used in training and tests.

## High-level data flow (step-by-step)

1. Input: a PDF or image medical report uploaded by a user.
2. OCR: `ocr_service.py` runs PDF/text extraction; if PDF is scanned it converts pages to images and runs Tesseract OCR.
3. Parsing: extracted text is fed into `medical_parser.py` which extracts `name`, `age`, `gender`, and biomarker values using regex-based patterns.
   - Note: Age extraction logic was improved to prefer plausible values (e.g., `Age/Sex : 50 Yr /F`).
4. Classification: parsed text (or extracted fields) can be passed to `bert_services.py` to detect conditions like diabetes, heart disease, etc.
5. Diet generation: `diet_generator.py` uses detected conditions + biomarkers + optional LLM (`gpt_service.py` or `llm_service.py`) to create personalized diet recommendations.
6. Frontend: the results are displayed by the UI in `frontend/app.py` and/or returned as JSON by backend routes in `backend/app/routes/`.

## Key components and responsibilities

- `ocr_service.py`
  - Uses `pdfplumber` for text-based PDFs, `pdf2image` + Tesseract (`pytesseract`) for scanned PDFs or images.
  - Returns a cleaned text blob for downstream parsing.
- `medical_parser.py`
  - Uses robust regex patterns to extract demographics and biomarkers.
  - Computes a simple risk score from conditions and biomarkers.
- `bert_services.py` (models directory exists under `backend/app/models/`)
  - Loads pretrained BERT-like models for disease detection.
  - Exposes inference helpers to classify text into condition labels.
- `diet_generator.py`
  - Encapsulates the rules for diet recommendations per condition.
  - Optionally enriches or reformats recommendations using the LLM helper.
- `gpt_service.py` / `llm_service.py`
  - Abstracts calls to any LLM used to refine natural-language output.

## How the pieces connect (example request)

1. User uploads `report.pdf`.
2. Backend route (e.g., `backend/app/routes/upload.py`) receives file bytes and calls `ocr_service.extract_text(bytes, filename)`.
3. OCR text goes to `medical_parser.extract_patient_info(text)` and `extract_biomarkers(text)`.
4. Parsed fields and full text are passed to `bert_services` for condition classification.
5. `diet_generator.generate(patient_info, conditions, biomarkers)` returns a structured diet plan.
6. Response sent back to the frontend or saved to DB; frontend renders summary and downloadable report.

Accuracy Targets
├── Disease Detection: > 85% accuracy
├── Biomarker Extraction: > 95% accuracy
├── Patient Info Parsing: > 90% accuracy
└── Diet Plan Relevance: > 80% user satisfaction

Reliability Targets
├── Uptime: > 99% availability
├── Error Rate: < 1% of requests
├── Response Time: < 30 seconds
└── Data Security: 100% compliance

```
## 🔧 Technical Implementation

- **Smart Parsing**: Automatically detects day headers, meal sections, and general notes
- **Icon Assignment**: Context-aware icons for different meal types
- **Responsive Design**: Works on desktop and mobile devices
- **Accessibility**: Clear visual hierarchy and readable fonts

## 📊 Benefits for Patients

1. **Easy to Follow**: Clear day-by-day structure
2. **Visual Appeal**: Color-coded sections prevent confusion
3. **Complete Information**: Portion sizes and preparation notes
4. **Professional Look**: Builds trust in the AI recommendations
5. **Mobile Friendly**: Easy to read on phones and tablets

---

**Result**: Patients and healthcare providers can now easily understand and follow the personalized diet plans generated by AI-NutriCare! 🎉
```
