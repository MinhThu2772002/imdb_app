import React, { useState, useEffect } from "react";
import axios from "axios";

const AverageRating = ({ actorId }) => {
  const [averageRating, setAverageRating] = useState(0);

  useEffect(() => {
    const fetchAverageRating = async () => {
      try {
        const response = await axios.get(
          `/api/actors/${actorId}/average-rating`
        );
        setAverageRating(response.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchAverageRating();
  }, [actorId]);

  return (
    <div>
      <h2>Average Rating</h2>
      <p>{averageRating}</p>
    </div>
  );
};

export default AverageRating;
