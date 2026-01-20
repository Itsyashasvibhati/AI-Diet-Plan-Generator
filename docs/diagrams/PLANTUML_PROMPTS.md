# PlantUML Prompts for AI-NutriCare

This file contains the PlantUML source prompts for the project's architecture, sequence flow, and deployment diagrams. Paste each block into a `.puml` file or a PlantUML editor to render.

## Architecture

```puml
@startuml
title AI-NutriCare - System Architecture
skinparam componentStyle rectangle

package "Frontend" {
  [Streamlit App]
}

package "Backend" {
  [FastAPI API]
  [Service Layer]
  [Model Orchestrator]
}

package "AI / Models" {
  [BERT Disease Classifier]
  [GPT Diet Generator]
}

package "External" {
  [OpenAI API]
  [Model Storage]
}

[Streamlit App] --> [FastAPI API] : HTTP (POST /upload)
[FastAPI API] --> [Service Layer] : send file
[Service Layer] --> [Model Orchestrator] : request inference
[Model Orchestrator] --> [BERT Disease Classifier] : predict
[Model Orchestrator] --> [GPT Diet Generator] : generate
[GPT Diet Generator] --> [OpenAI API] : REST call
[FastAPI API] --> [Model Storage] : load / cache models
@enduml
```

## Sequence (Upload → Processing → Response)

```puml
@startuml
title AI-NutriCare - Upload & Processing Sequence
actor User
participant "Streamlit\nFrontend" as Frontend
participant "FastAPI\nBackend" as Backend
participant "OCR Service" as OCR
participant "Parser Service" as Parser
participant "BERT Model" as BERT
participant "GPT Service" as GPT

User -> Frontend: Upload medical report (PDF/JPG/PNG)
Frontend -> Backend: POST /upload (multipart/form-data)
Backend -> Backend: Validate file & store (temp)
Backend -> OCR: Extract text from document
OCR --> Backend: clean_text
Backend -> Parser: Extract biomarkers & patient info
Parser --> Backend: biomarkers_json
Backend -> BERT: Classify conditions (inference)
BERT --> Backend: condition_probabilities
Backend -> GPT: Generate diet plan (prompt with context)
GPT --> Backend: diet_plan_text
Backend -> Frontend: JSON response (biomarkers, conditions, diet_plan)
Frontend -> User: Display results (tabs, charts, download)

@enduml
```

## Deployment (Render + Containers)

```puml
@startuml
title AI-NutriCare - Deployment Overview
cloud "Render" {
  node "Frontend Service" {
    [Streamlit Container]
  }
  node "Backend Service" {
    [FastAPI Container]
    [Worker / Async Queue]
  }
  node "Model Volume" {
    [Model Files (BERT, RF)]
  }
}

[Streamlit Container] --> [FastAPI Container] : HTTP (POST/GET)
[FastAPI Container] --> [Model Files (BERT, RF)] : read / cache
[FastAPI Container] --> "OpenAI API" : REST (GPT)
note right of [FastAPI Container]
  Env vars / Secrets managed by Render
  Persistent disk for large models
end note
@enduml
```
