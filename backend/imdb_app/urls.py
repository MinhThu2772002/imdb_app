from django.urls import path
from imdb_app.router import actors, movies

urlpatterns = [
    path('actors/', actors.actors, name='actors'),
    path('movies/', movies.movies, name='movies'),
]