# Fast API framework
from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Dotenv
from dotenv import load_dotenv
load_dotenv()
import os 


# API Routes
from routes import actors, movies

app = FastAPI()

# Define the origins that are allowed to make cross-origin requests
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
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
from db import database
@app.on_event("startup")
async def startup():
    await database.database.connect()
    database.metadata.create_all(bind=database.engine)
    print("Database connected")
@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


# Include routers
app.include_router(actors.ActorsRoute)
app.include_router(movies.MovieRoute)

    