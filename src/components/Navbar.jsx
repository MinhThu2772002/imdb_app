import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar" role="navigation" aria-label="main navigation">
      <div className="navbar-brand">
        <Link className="navbar-item" to="/">
          Home
        </Link>
      </div>

      <div className="navbar-menu">
        <div className="navbar-start">
          <Link className="navbar-item" to="/actors">
            Actors/Actresses
          </Link>
          {/* Add links for other functionalities */}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
