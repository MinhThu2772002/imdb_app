from fastapi import APIRouter
from db import database
from db import models
import requests
import os
from bs4 import BeautifulSoup
import re
MovieRoute = APIRouter()

@MovieRoute.get("/movies")
async def get_movies(id: str = None):
    db = database.SessionLocal()
    if id is None:
        movies = db.query(models.Movie).all()
        return movies
    else: 
        movie = db.query(models.Movie).filter(models.Movie.movie_id == id).first()
        return movie
@MovieRoute.put("/movies")
async def Scrape_movie():
    db = database.SessionLocal()
    actors = db.query(models.Actors).all()
    actors_bio_url = []
    for actor in actors:
        url = getattr(actor, "bio_url")
        actors_bio_url.append(url)
    for url in actors_bio_url:
        actor_page = requests.get(url, 'hmtl-parser',headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
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
                except ValueError:
                    average_rating = None
            movie = db.query(models.Movie).filter(models.Movie.movie_name == movie_name).first()
            if movie is None:
                movie = models.Movie(movie_name=movie_name, release_year=release_year, average_rating=average_rating)
                db.add(movie)
  
            else:
                movie.release_year = release_year
                movie.average_rating = average_rating
            db.commit()
            db.refresh(movie)

    return {"message": "Scrape Complete"} 
        