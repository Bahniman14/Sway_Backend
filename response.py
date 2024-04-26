from fastapi import APIRouter, Depends
from App import app
from connection import conn
# app = FastAPI()
from database import return_profile
router = APIRouter()

@router.get("/Profile")
async def profile(user_id : str):
    
    profile_data = return_profile(conn, user_id)
    # hard code
    # print(f"profile user_id : {user_id}")
    # # Some logic to fetch profile data based on user_id
    # profile_data = {
    #     "username": "@BG",
    #     "photoURL": "PH01",
    #     "about_me": "Python Developer"
    # }
    print(profile_data)
    return profile_data
    
app.include_router(router)