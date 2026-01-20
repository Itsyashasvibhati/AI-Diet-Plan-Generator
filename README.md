# 📋 **AI-NutriCare Project Report**

## 🎯 **Project Overview**

**AI-NutriCare** is an advanced AI-powered diet planning system that analyzes medical reports and generates personalized diet plans based on detected diseases and biomarker values. The system uses machine learning and natural language processing to provide healthcare professionals and patients with intelligent nutritional recommendations.

**Key Technologies**: FastAPI, Streamlit, BERT, GPT, Scikit-learn, PyTorch

---

## 🎨 **Frontend Architecture & Design**

### **📚 Libraries Used**
![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/cce2ac6aae3d2ca1a7b1f2c8c128ca9aea5f4d68/Screenshot%202026-01-19%20104425.png)
### **📚 Libraries Used**
#### **Primary Framework**

- **Streamlit** (`streamlit==1.28.1`): Main web framework for building the interactive UI
  - Provides reactive components and easy deployment
  - Handles file uploads, progress bars, and real-time updates

#### **Supporting Libraries**

- **Requests** (`requests==2.31.0`): HTTP client for API communication with backend
- **Pillow** (`pillow==10.1.0`): Image processing for file uploads
- **Python-dotenv** (`python-dotenv==1.0.0`): Environment variable management

### **🎯 Key Frontend Functions & Features**

![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/fb757874ddab7a8c5c8006a3b7ba24bfde11fb62/Screenshot%202026-01-19%20104509.png)




![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/85152998686ee4e34346aa7f630ffb78444aa06f/Screenshot%202026-01-19%20104542.png)

![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/bf0d84b009d881e17b9b142400c02e24aa234edc/Screenshot%202026-01-19%20104600.png)
## 🔧 **Backend Architecture & Model Training**

![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/103464c1e3aef5eedd2425d3c8defb6cad4b1af4/flowdiagram.png)


![image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/96963519a1b1ba392e5ad0bc0f10b875209404c6/sequencesDiagram.png)

**Output Structure**:

- **7-Day Plan**: Breakfast, Lunch, Dinner, Snacks
- **Portion Control**: Specific quantities
- **Nutritional Balance**: Macronutrient distribution
- **Condition-Specific**: Tailored to medical needs


## 📁 **Project Structure**


```
AI-Diet-Plan-Generator/
├── backend/                          # FastAPI backend
│   ├── app/
│   │   ├── main.py                   # FastAPI application
│   │   ├── config.py                 # Configuration management
│   │   ├── models/                   # Pydantic models
│   │   ├── routes/                   # API endpoints
│   │   │   ├── upload.py            # File upload endpoint
│   │   │   ├── diet.py              # Diet plan routes
│   │   │   └── predict.py           # Prediction routes
│   │   └── services/                # Business logic
│   │       ├── bert_services.py     # BERT model integration
│   │       ├── diet_generator.py    # Diet plan logic
│   │       ├── gpt_service.py       # OpenAI integration
│   │       ├── medical_parser.py    # Biomarker extraction
│   │       ├── ocr_service.py       # Document processing
│   │       └── preprocessing.py     # Text cleaning
│   └── requirements.txt             # Python dependencies
├── frontend/                         # Streamlit frontend
│   ├── app.py                       # Main Streamlit application
│   └── requirements.txt             # Frontend dependencies
├── training/                        # Model training scripts
│   ├── train_bert.py               # BERT model training
│   ├── train_ml_model.py           # Traditional ML training
│   ├── tune_bert_hyperparams.py    # Hyperparameter tuning
│   └── data/                       # Training datasets
├── data/                           # Data processing
│   ├── raw/                        # Raw medical datasets
│   └── processed/                  # Cleaned training data
└── scripts/                        # Utility scripts
    ├── create_nutrition_guidelines.py
    └── extract_numeric.py
```

---



Data Flow Diagram(Level 0)

![Image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/a66fc156e055b6e86922f1084c21cc60488d4301/DFDlevel0.png)


Data Flow Diagram(Level 1)

![image](https://github.com/Itsyashasvibhati/AI-Diet-Plan-Generator/blob/dbaed0c07900f7adf1fb2d56fd8b51561728e122/DFDlevel1.png)


## 🔧 **Setup & Deployment**

### **Local Development**

```bash
# Backend setup
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

# Frontend setup
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### **Production Deployment**

- **Platform**: Render (Docker-based)
- **Backend**: FastAPI with Uvicorn
- **Frontend**: Streamlit web app
- **Database**: File-based (can be upgraded to PostgreSQL)

### **System Requirements**

- **Python**: 3.10+
- **Memory**: 4GB+ for model inference
- **Storage**: 10GB+ for models and data
- **External APIs**: OpenAI API key required

---


## 🔮 **Future Enhancements**

- **Database Integration**: PostgreSQL for user management
- **Advanced ML Models**: Custom transformer architectures
- **Multi-language Support**: International medical reports
- **Integration APIs**: EHR system connectivity
- **Mobile App**: Native iOS/Android applications
- **Real-time Monitoring**: Patient progress tracking

---

## 📚 **Learning Outcomes**

This project demonstrates expertise in:

- **Full-Stack Development**: FastAPI backend + Streamlit frontend
- **Machine Learning**: BERT fine-tuning and ensemble methods
- **Natural Language Processing**: Medical text analysis
- **API Integration**: OpenAI GPT and cloud services
- **Data Processing**: Medical document parsing and biomarker extraction
- **UI/UX Design**: Professional healthcare interface
- **DevOps**: Docker containerization and cloud deployment

---



**Technologies Used**:

- Frontend: Streamlit, HTML/CSS, JavaScript
- Backend: FastAPI, Python
- AI/ML: BERT, GPT-3.5, Scikit-learn
- Data Processing: OCR, PDF parsing, Text analysis
- Deployment: Render Cloud Platform

---

