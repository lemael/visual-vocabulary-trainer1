import axios from "axios";
import React, { useEffect, useState } from "react";
import "./LoginPage.css"; // Si vous avez un fichier CSS spécifique

const LoginPage = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/login/",
        {
          username,
          password,
        },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          withCredentials: true,
        }
      );
      console.log(response.data);
      // Rediriger l'utilisateur ou mettre à jour l'état de l'application ici
    } catch (error) {
      setError("Invalid credentials");
    }
  };

  useEffect(() => {
    fetch("/login.html")
      .then((response) => response.text())
      .then((data) => setHtmlContent(data));
  }, []);

  return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
};

export default LoginPage;
