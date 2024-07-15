import React, { useEffect, useState } from "react";
import "./HomePage.css";

const HomePage = () => {
  const [htmlContent, setHtmlContent] = useState("");

  useEffect(() => {
    fetch("/homePage.html")
      .then((response) => response.text())
      .then((data) => setHtmlContent(data));
  }, []);

  return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
};

export default HomePage;
