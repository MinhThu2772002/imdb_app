from fastapi import APIRouter
from db import database
from db import models
import requests
import os
from bs4 import BeautifulSoup
ActorsRoute = APIRouter()

@ActorsRoute.get("/actors")
async def Get_actors(name: str = None):
    db = database.SessionLocal()
    if name:
        results = db.query(models.Actors).filter(models.Actors.actor_name == name).all()
    else:
        results = db.query(models.Actors).all()
    if results:
        return {"message": "Get actors information successfully", "data": results}
    else:
        return {"message": "No actors found"}

@ActorsRoute.put("/actors")
async def Scape_the_list_of_actors_and_details():
    db = database.SessionLocal()
    pages = requests.get(os.environ.get('actors_url'))
    soup = BeautifulSoup(pages.text, 'html.parser')
    list_of_actors = soup.find_all('div', class_="lister-item mode-detail")
    for actor in list_of_actors:
        name = actor.find('h3', class_= "lister-item-header").find('a').text
        biography = actor.find('div', class_="lister-item-image").find('img').get('src')
        birth_info = actor.find('h3', class_= "lister-item-header").find('a').get('href')[6:]
        link = f"https://www.imdb.com/name/{birth_info}/bio/?ref_=nm_ov_bio_sm".format(birth_info=birth_info)
        birth_page = requests.get(link, 'html.parser', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
        birth_page = BeautifulSoup(birth_page.text, 'html.parser')
        birth_info = birth_page.find('section', class_="ipc-page-section ipc-page-section--base").find('ul').find_all('li')[0].find_all('a')
        birth_date = birth_info[0].text + " " + birth_info[1].text
        bind_place = birth_info[2].text
        actor = db.query(models.Actors).filter(models.Actors.actor_name == name).first()
        if actor:
            updated_data = {
                'actor_name': name[1:-1],
                'biography': biography,
                'birth_date': birth_date,
                'birth_place': bind_place,
                'bio_url': link
            }
            for key, value in updated_data.items():
                setattr(actor, key, value)  # Update the corresponding attributes with the new values
        else:
            actor = models.Actors(
                actor_name = name[1:-1],
                biography = biography,
                birthdate = birth_date,
                birthplace = bind_place,
                bio_url = link
            )
            db.add(actor)
        db.commit()
        db.refresh(actor)
    return {"message": "success"}