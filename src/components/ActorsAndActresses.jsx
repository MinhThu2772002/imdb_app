import React, { useState, useEffect } from "react";
import axios from "axios";

const ActorsAndActresses = () => {
  const [actors, setActors] = useState([]);

  useEffect(() => {
    const fetchActors = async () => {
      try {
        const response = await axios.get("/api/actors");
        setActors(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchActors();
  }, []);

  return (
    <div>
      <h2>Actors and Actresses</h2>
      <ul>
        {actors.map((actor) => (
          <li key={actor.id}>
            <a href={`/actor/${actor.id}`}>{actor.name}</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActorsAndActresses;
