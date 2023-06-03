from fastapi import APIRouter
from db import database
from db import models


UserRoute = APIRouter()

@UserRoute.get("/actors")
async def getActors(id: int = None):
    db = database.SessionLocal()
    if id:
        results = db.query(models.Actors).get(id)
    else:
        results = db.query(models.Actors).all()
    return results
