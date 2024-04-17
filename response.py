from fastapi import APIRouter
from App import app
# app = FastAPI()
router = APIRouter()

@router.get("/Profile")
async def profile(user_id: str):
    print(f"profile user_id : {user_id}")
    # Some logic to fetch profile data based on user_id
    profile_data = {
        "username": "@BG",
        "photoURL": "PH01",
        "about": "Python Developer"
    }
    return profile_data

app.include_router(router)