import React, { useEffect, useState } from "react";
import axios from "axios";

const ActorsAndActresses = () => {
  const [actors, setActors] = useState([]);

  useEffect(() => {
    // Fetch the list of actors and actresses from the backend API
    const fetchActors = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/actors", {
          headers: {
            Accept: "application/json",
          },
        });
        const data = response.data;
        console.log(data);
        setActors(data);
      } catch (error) {
        console.error("Error fetching actors: ", error);
      }
    };

    fetchActors();
  }, []);

  return (
    <div className="container">
      <h2 className="title is-2">List of Actors and Actresses</h2>
      <div className="columns is-multiline">
        {actors.map((actor) => (
          <div key={actor.actor_id} className="column is-one-third">
            <div className="card">
              <div className="card-image">
                <figure className="image is-4by3">
                  <img src={actor.biography} alt={actor.actor_name} />
                </figure>
              </div>
              <div className="card-content">
                <p className="title is-4">{actor.actor_name}</p>
                <p className="subtitle is-6">Born: {actor.birthdate}</p>
                <p className="subtitle is-6">Birthplace: {actor.birthplace}</p>
                <div className="content">
                  <a
                    href={actor.bio_url}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Biography
                  </a>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ActorsAndActresses;
