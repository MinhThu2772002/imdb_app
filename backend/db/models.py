from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Actors(Base):
    __tablename__ = "Actors"

    actor_id = Column(Integer, primary_key=True)
    actor_name = Column(String(255))
    biography = Column(String)
    birthdate = Column(String(255))
    birthplace = Column(String(255))

class Movie(Base):
    __tablename__ = "Movie"

    movie_id = Column(Integer, primary_key=True)
    movie_name = Column(String(255))
    release_year = Column(Integer)
    average_rating = Column(String(255))

class ActorMovie(Base):
    __tablename__ = "ActorMovie"

    actor_id = Column(Integer, ForeignKey('Actors.actor_id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('Movie.movie_id'), primary_key=True)

class Award(Base):
    __tablename__ = "Award"

    award_id = Column(Integer, primary_key=True)
    award_name = Column(String(255))
    year = Column(Integer)
    movie_id = Column(Integer, ForeignKey('Movie.movie_id'))
    actor_id = Column(Integer, ForeignKey('Actors.actor_id'))

class Genre(Base):
    __tablename__ = "Genre"

    genre_id = Column(Integer, primary_key=True)
    genre_name = Column(String(255))

class MovieGenre(Base):
    __tablename__ = "MovieGenre"

    movie_id = Column(Integer, ForeignKey('Movie.movie_id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('Genre.genre_id'), primary_key=True)

    movie = relationship("Movie", backref="movie_genres")
    genre = relationship("Genre", backref="genre_movies")

class Rating(Base):
    __tablename__ = "Rating"
    movie_id = Column(Integer, ForeignKey('Movie.movie_id'), primary_key=True)
    year = Column(Integer)
    

