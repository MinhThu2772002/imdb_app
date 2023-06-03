import React, { useState, useEffect } from "react";
import axios from "axios";

const Awards = ({ actorId }) => {
  const [awards, setAwards] = useState([]);

  useEffect(() => {
    const fetchAwards = async () => {
      try {
        const response = await axios.get(`/api/actors/${actorId}/awards`);
        setAwards(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchAwards();
  }, [actorId]);

  return (
    <div>
      <h2>Awards</h2>
      <ul>
        {awards.map((award) => (
          <li key={award.id}>
            {award.name} - {award.year} ({award.movie})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Awards;
