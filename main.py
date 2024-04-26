# from fastapi import FastAPI
from update import app as update_app
from response import app as response_app
from fastapi.middleware.cors import CORSMiddleware
from App import app
# from database import create_connection
from connection import conn

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
