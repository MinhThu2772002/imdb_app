from fastapi import APIRouter
from db import database
from db import models
import requests
from bs4 import BeautifulSoup
route = APIRouter()

@route.put("/awards")
def Scape_the_awards_of_actors_and_corresponding_movies():
    db = database.SessionLocal()
    actors = db.query(models.Actors).all()
    # i = 1
    for actor in actors:
        print(actor.actor_name)

        code =actor.bio_url.split("/")[4]
        award_url = f"https://www.imdb.com/name/{code}/awards/?ref_=nm_ql_2"
        award_response = requests.get(award_url, 'html.parser', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'})
        award_soup = BeautifulSoup(award_response.text, "html.parser")
        sections = award_soup.find_all("section", class_="ipc-page-section ipc-page-section--base")[:-1]
        for section in sections:
            award_name = section.find('h3').text
            movies = section.find_all('a', class_='ipc-metadata-list-summary-item__li ipc-metadata-list-summary-item__li--link')
            for movie in movies:
                print(movie.text)
        return