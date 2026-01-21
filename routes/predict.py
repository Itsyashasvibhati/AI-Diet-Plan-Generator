from fastapi import APIRouter
from app.services.bert_services import predict_disease

router = APIRouter()

@router.post("/")
def predict_disease_api(payload: dict):
    text = payload.get("text", "")
    if not text:
        return {"predicted_disease": []}

    conditions = predict_disease(text)
    return {"predicted_disease": conditions}
