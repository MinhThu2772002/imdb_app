import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "bulma/css/bulma.min.css";
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import ActorsAndActresses from "./components/ActorsAndActresses";
import ActorDetails from "./components/ActorDetails";
import Movies from "./components/Movies";
import Awards from "./components/Awards";
import Genres from "./components/Genres";
import AverageRating from "./components/AverageRating";
import TopMovies from "./components/TopMovies";

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Routes>
          <Route exact path="/" element={<HomePage />} />{" "}
          <Route path="/actors" element={<ActorsAndActresses />} />{" "}
          <Route path="/actor/:id" element={<ActorDetails />} />{" "}
          <Route path="/movies/:id" element={<Movies />} />{" "}
          <Route path="/awards/:id" element={<Awards />} />{" "}
          <Route path="/genres/:id" element={<Genres />} />{" "}
          <Route path="/average-rating/:id" element={<AverageRating />} />{" "}
          <Route path="/top-movies/:id" element={<TopMovies />} />{" "}
        </Routes>{" "}
      </div>{" "}
    </Router>
  );
};

export default App;
