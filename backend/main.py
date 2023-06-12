# Fast API framework
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Dotenv
from dotenv import load_dotenv
load_dotenv()
import os 


# API Routes
from routes import actors, movies, awards

app = FastAPI()

# Define the origins that are allowed to make cross-origin requests
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
    "https://rapidapi.com",
    # Add more origins as needed
]

# Add the CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to database
from db import database, models
@app.on_event("startup")
async def startup():
    await database.database.connect()
    models.Base.metadata.create_all(database.engine)
    print("Database connected")
@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


# Include routers
app.include_router(actors.route)
app.include_router(movies.route)
app.include_router(awards.route)

    