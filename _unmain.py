from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import json

# app = FastAPI()

# CORS middleware to allow requests from any origin
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# SQLAlchemy configuration
# DATABASE_URL = "sqlite:///./mydatabase.db"
# engine = create_engine(DATABASE_URL)
# metadata = MetaData()

# Define a table for storing data
# scores = Table(
#     "scores",
#     metadata,
#     Column("id", Integer, primary_key=True, index=True),
#     Column("name", String),
#     Column("score", Integer),
# )

# Create the table
# metadata.create_all(bind=engine)


# Pydantic model for request payload
# class ScoreUpdate(BaseModel):
#     score: int
#     name: str
#     id: int
# class GetUpdate(BaseModel):
#     id: int
# FastAPI endpoint to update the score
# @app.post("/update-score")
# async def update_score(score_data: ScoreUpdate):
#     # Access score and name from the Pydantic model
#     score = score_data.score
#     name = score_data.name
#     id = score_data.id
#     # Store data in the database
#     print(f"Name: {name}, Score: {score}, ID Number: {id}")
#     with Session(engine) as session:
#         session.execute(scores.insert().values(score=score, name=name, id=id))
#         session.commit()

#     return {"message": "Score and Name received successfully"}

# @app.post("/get-update")
# async def get_update(get_data: GetUpdate):
#     id = get_data.id
#     print(f"Request Submitted for ID {id}")

#     # Retrieve data from the database
#     with Session(engine) as session:
#         query = select(scores).where(scores.c.id == id)
#         result = session.execute(query)
#         data = result.fetchone()
#         print(data, data.score, data.name)
#     if data:
#         data_dict = data._asdict()  # Convert the SQLAlchemy Row to a dictionary
#         print(data_dict)
#         # Serialize the dictionary to JSON
#         json_data = json.dumps(data_dict)
#         return json_data
#     else:
#         raise HTTPException(status_code=404, detail=f"Data not found for ID: {id}")