from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/diet", tags=["Diet Generator"])

class DietRequest(BaseModel):
    age: int
    weight: float
    height: float
    condition: str
    goal: str
    diet_type: str

@router.post("/generate")
def generate_diet(data: DietRequest):
    # STEP 1: Read user input
    condition = data.condition.lower()
    goal = data.goal.lower()
    diet_type = data.diet_type.lower()

    # STEP 2: Rule-based logic (can later replace with AI)
    breakfast = []
    lunch = []
    dinner = []
    avoid = []

    if condition == "diabetes":
        avoid += ["Sugar", "White bread", "Soft drinks"]
        breakfast += ["Oats", "Boiled eggs", "Green tea"]
        lunch += ["Brown rice", "Vegetables", "Salad"]
        dinner += ["Soup", "Grilled vegetables"]

    if goal == "weight_loss":
        breakfast.append("Fruit (low sugar)")
        dinner = ["Light soup", "Salad"]

    if diet_type == "veg":
        breakfast = [item for item in breakfast if "egg" not in item.lower()]

    # STEP 3: Final diet plan
    diet_plan = {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner,
        "avoid": avoid,
        "notes": "Personalized diet generated based on health condition and goal."
    }

    return diet_plan
