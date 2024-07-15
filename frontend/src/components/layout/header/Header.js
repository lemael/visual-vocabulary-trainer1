import React, { useContext } from "react";
import "./Header.css"; // Si vous avez des styles spécifiques pour l'en-tête.
import { AuthContext } from "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/AuthContext";
const Header = () => {
  const { isAuthenticated, username, role, logout } = useContext(AuthContext);
  return (
    <head>
      <meta charset="utf-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta
        name="viewport"
        content="width=device-width, initial-scale=1, shrink-to-fit=no"
      />
      <title>Digitalfabrik - Visueller Fachwortschatz-Trainer</title>
      <link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      {isAuthenticated ? (
        <>
          <div class="ml-auto">
            <button type="submit" class="btn btn-dark border border-white">
              <a href="/logout" class="text-white text-decoration-none">
                Logout
              </a>
            </button>
          </div>
        </>
      ) : (
        <>
          <div class="ml-auto">
            <a
              href="/register"
              class="btn btn-dark text-white text-decoration-none border border-white"
            >
              Register
            </a>
            <a
              href="/login"
              class="btn btn-dark text-white border border-white"
            >
              Login
            </a>
          </div>
        </>
      )}
    </head>
  );
};
export default Header;
