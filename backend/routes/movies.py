from fastapi import APIRouter
from db import database
from db import models
import requests
import os
from bs4 import BeautifulSoup
import re
route = APIRouter()

@route.get("/movies/")
async def get_movies(actor_name: str = None):
    db = database.SessionLocal()
    if actor_name is None:
        movies = db.query(models.Movie).all()
        if movies:
            return {"message": "Get movies successfully", "data": movies}
        else: return {"message": "No movies found"}
    else: 
        movies = (
            db.query(models.Movie)
            .join(models.ActorMovie)
            .join(models.Actors)
            .filter(models.Actors.actor_name == actor_name)
            .all()
        )
        if movies:
            return {"message": "Get movies successfully", "data": movies}

@route.put("/movies")
async def Scrape_the_list_of_movie_based_on_actors_list():
    db = database.SessionLocal()
    actors = db.query(models.Actors).all()
    actors_id_url = []
    for actor in actors:
        url = getattr(actor, "bio_url")
        id = getattr(actor, "actor_id")
        actors_id_url.append({'url': url, 'id': id})
    i = 1
    for actor in actors_id_url:
        actor_page = requests.get(actor['url'], 'hmtl-parser',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
        soup = BeautifulSoup(actor_page.text, 'html.parser').find_all('section', class_="ipc-page-section ipc-page-section--base")[6].find('ul').find_all('li')
        for film in soup:
            film = film.find('a')
            movie_name = film.text
            release_year = film.parent.text[(film.parent.text.find('(') + 1):film.parent.text.find(')')]
            rating_page = requests.get('https://www.imdb.com/'+film['href'], 'hmtl-parser',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
            try:
                average_rating = BeautifulSoup(rating_page.text, 'html.parser').find_all('span', class_="ipc-btn__text")[6].text[:3]
            except IndexError:
                average_rating = None
            if average_rating is not None:
                try:
                    average_rating = float(average_rating)
                    if average_rating > 10: 
                        raise ValueError
                except ValueError:
                    average_rating = None
            movie = db.query(models.Movie).filter(models.Movie.movie_name == movie_name).first()
            if movie is None:
                movie = models.Movie(movie_name=movie_name, release_year=release_year, average_rating=average_rating)
                db.add(movie)
                db.commit()
                movie_actor = models.ActorMovie(actor_id=actor['id'], movie_id=movie.movie_id)
                db.add(movie_actor)
            else:
                movie.release_year = release_year
                movie.average_rating = average_rating
            db.commit()
            db.refresh(movie)
    return {"message": "Scrape Complete"} 
        