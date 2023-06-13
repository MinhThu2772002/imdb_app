from rest_framework import serializers
from .models import Actors, Movie, ActorMovie, Award, Genre, MovieGenre, Rating

class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ('actor_name', 'biography', 'birthdate', 'birthplace', 'bio_url')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_name', 'release_year', 'average_rating')

class ActorMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorMovie
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieGenre
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'