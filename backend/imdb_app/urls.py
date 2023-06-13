from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actors, name='actors'),
    path('actors/<str:actor_id>/', views.actors, name='actors_by_name'),
    # path('movies/', views.movies, name='movies'),
    # path('movies/<str:actor_name>/', views.movies, name='movies_by_name')
]