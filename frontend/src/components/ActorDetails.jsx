import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const ActorDetails = () => {
  const { id } = useParams();
  const [actor, setActor] = useState(null);

  useEffect(() => {
    const fetchActorDetails = async () => {
      try {
        const response = await axios.get(`/api/actors/${id}`);
        setActor(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchActorDetails();
  }, [id]);

  return (
    <div>
      {actor ? (
        <div>
          <h2>{actor.name}</h2>
          <p>Biography: {actor.biography}</p>
          <p>Birthdate: {actor.birthdate}</p>
          <p>Birthplace: {actor.birthplace}</p>
          {/* Add more details as needed */}
        </div>
      ) : (
        <p>Loading actor details...</p>
      )}
    </div>
  );
};

export default ActorDetails;
