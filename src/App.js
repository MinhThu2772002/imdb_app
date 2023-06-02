import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
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
      <Routes>
        <Route exact path="/" component={HomePage} />{" "}
        <Route path="/actors" component={ActorsAndActresses} />{" "}
        <Route path="/actor/:id" component={ActorDetails} />{" "}
        <Route path="/movies/:id" component={Movies} />{" "}
        <Route path="/awards/:id" component={Awards} />{" "}
        <Route path="/genres/:id" component={Genres} />{" "}
        <Route path="/average-rating/:id" component={AverageRating} />{" "}
        <Route path="/top-movies/:id" component={TopMovies} />{" "}
      </Routes>{" "}
    </Router>
  );
};

export default App;
