import React from "react";
import { Link } from "react-router-dom";
import backgroundImage from "./background.jpg"; // Import the background image

const HomePage = () => {
  const backgroundStyle = {
    backgroundImage: `url(${backgroundImage})`,
    backgroundSize: "cover",
    backgroundPosition: "center",
    backgroundRepeat: "no-repeat",
    height: "100vh",
  };
  return (
    <div className="homepage" style={backgroundStyle}>
      <div className="homepage-content">
        <div className="container">
          <div className="columns">
            <div className="column is-half is-offset-one-quarter">
              <div className="box" style={{ marginTop: "100px" }}>
                <h1 className="title has-text-centered">
                  Welcome to IMDb Character Software
                </h1>
                <p className="subtitle has-text-centered">
                  The project involves creating a user-friendly software
                  application that focuses on storing and extracting information
                  about the top 50 popular Hollywood actors and actresses. The
                  data will be sourced from the IMDb website and will include
                  details such as actor/actress names, movie information,
                  awards, genres, and ratings.
                </p>
                <div className="has-text-centered">
                  <Link to="/actors" className="button is-primary">
                    Let's explore
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
