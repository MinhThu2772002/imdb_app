from django.db import models

# Create your models here.

class Actors(models.Model):
    actor_id = models.AutoField(primary_key=True)
    actor_name = models.CharField(max_length=255)
    biography = models.TextField()
    birthdate = models.CharField(max_length=255)
    birthplace = models.CharField(max_length=255)
    bio_url = models.TextField()

    def __str__(self):
        return self.actor_name
    
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=255)
    release_year = models.CharField(max_length=255)
    average_rating = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.movie_name

class ActorMovie(models.Model):
    actor_id = models.ForeignKey(Actors, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.actor_id
    
class Award(models.Model):
    award_id = models.AutoField(primary_key=True)
    award_name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(Actors, on_delete=models.CASCADE)

    def __str__(self):
        return self.award_name

class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_name

class MovieGenre(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Rating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    year = models.CharField(max_length=255)