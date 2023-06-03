# Fast API framework
from typing import Union
from fastapi import FastAPI



# Dotenv
from dotenv import load_dotenv
load_dotenv()
import os 


# API Routes
from routes import users, update

app = FastAPI()


# Connect to database
from db import database
@app.on_event("startup")
async def startup():
    await database.database.connect()
    print("Database connected")
@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


# Include routers
app.include_router(users.UserRoute)
app.include_router(update.update_router)

    