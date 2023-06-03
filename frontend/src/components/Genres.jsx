import React, { useState, useEffect } from "react";
import axios from "axios";

const Genres = ({ actorId }) => {
  const [genres, setGenres] = useState([]);

  useEffect(() => {
    const fetchGenres = async () => {
      try {
        const response = await axios.get(`/api/actors/${actorId}/genres`);
        setGenres(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchGenres();
  }, [actorId]);

  return (
    <div>
      <h2>Genres</h2>
      <ul>
        {genres.map((genre) => (
          <li key={genre.id}>{genre.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default Genres;
