from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status

from imdb_app.models import Actors, Movie, ActorMovie
from imdb_app.serializers import ActorsSerializer, MovieSerializer, ActorMovieSerializer

import requests
import os
from bs4 import BeautifulSoup


@api_view(['GET', 'PUT'])
def movies(request):
    name = request.GET.get('actor_name')
    if request.method == 'GET':
        if name is None:
            movies = Movie.objects.all()
            if movies:
                serializer = MovieSerializer(movies, many=True)
                return Response(serializer.data)
            else:
                return Response({'message: Movies not found'},status=status.HTTP_404_NOT_FOUND)
        else:
            try:
                actor = Actors.objects.get(actor_name=name)
                actor_movies = ActorMovie.objects.filter(actor_id=actor.actor_id)
                movies = Movie.objects.filter(actormovie__in=actor_movies)
                data = [{'movie_id': movie.movie_id, 'movie_name': movie.movie_name, 'release_year': movie.release_year, 'rating': movie.average_rating} for movie in movies]
                return JsonResponse(data, safe=False)
            except:
                return Response({'message: Movies not found'},status=status.HTTP_404_NOT_FOUND)
            
    if  request.method == 'PUT':
        actors = Actors.objects.all()
        actors_id_url = []
        for actor in actors:
            url = actor.bio_url
            id = actor.actor_id
            actors_id_url.append({'url': url, 'id': id})
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
                try:
                    movie = Movie.objects.get(movie_name=movie_name)
                    movie.release_year = release_year
                    movie.average_rating = average_rating
                    movie.save()
                except Movie.DoesNotExist:
                    # Actor does not exist, create a new instance
                    movie = Movie(movie_name=movie_name, release_year=release_year, average_rating=average_rating)
                    movie.save()
                    actor_id = (actor['id'])
                    actor_get = Actors.objects.get(actor_id=actor_id)
                    actor_movie = ActorMovie(actor_id=actor_get, movie_id=movie)
                    actor_movie.save()
        return Response({'message: Movies updated'},status=status.HTTP_201_CREATED)    
            