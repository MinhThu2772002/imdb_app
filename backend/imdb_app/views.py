from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status

from .models import Actors
from .serializers import ActorsSerializer
# Create your views here.


import requests
import os
from bs4 import BeautifulSoup


@api_view(['GET', 'PUT'])
def actors(request, name=None):
    if request.method == 'GET':
        if name is None:
            actors = Actors.objects.all()
            serializer = ActorsSerializer(actors, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            actors = Actors.objects.filter(actor_name=name)
            serializer = ActorsSerializer(actors, many=True)
            return JsonResponse(serializer.data, safe=False)
    if request.method == 'PUT':
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
            birth_place = birth_info[2].text
            
            try:
                # Check if the actor already exists in the database
                actor = Actors.objects.get(actor_name=name)
                # Update the actor's information
                actor.biography = biography
                actor.birthdate = birth_date
                actor.birthplace = birth_place
                actor.bio_url = link
                actor.save()
            except Actors.DoesNotExist:
                # Actor does not exist, create a new instance
                actor = Actors(actor_name=name, biography=biography, birthdate=birth_date, birthplace=birth_place, bio_url=link)
                actor.save()
        return Response({'message': 'Scrape successfully!!'}, status=status.HTTP_201_CREATED)