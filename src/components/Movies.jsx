import React, { useState, useEffect } from "react";
import axios from "axios";

const Movies = ({ actorId }) => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await axios.get(`/api/actors/${actorId}/movies`);
        setMovies(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchMovies();
  }, [actorId]);

  return (
    <div>
      <h2>Movies</h2>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            {movie.name} ({movie.year})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Movies;
