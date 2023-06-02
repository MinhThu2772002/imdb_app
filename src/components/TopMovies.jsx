import React, { useState, useEffect } from "react";
import axios from "axios";

const TopMovies = ({ actorId }) => {
  const [topMovies, setTopMovies] = useState([]);

  useEffect(() => {
    const fetchTopMovies = async () => {
      try {
        const response = await axios.get(`/api/actors/${actorId}/top-movies`);
        setTopMovies(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchTopMovies();
  }, [actorId]);

  return (
    <div>
      <h2>Top Movies</h2>
      <ul>
        {topMovies.map((movie) => (
          <li key={movie.id}>
            {movie.name} ({movie.year}) - {movie.genre}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TopMovies;
