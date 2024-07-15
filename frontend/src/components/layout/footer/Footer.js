import React from "react";
import "./Footer.css"; // Si vous avez des styles spécifiques pour le pied de page

const Footer = () => {
  return (
    <footer class="footer py-1 navbar navbar-expand-md fixed-bottom navbar-dark bg-dark">
      <div class="container mb-auto">
        <span class="text-muted">
          <a href="https://tuerantuer.de/digitalfabrik">
            Tür an Tür Digitalfabrik gGmbH
          </a>
        </span>
      </div>
    </footer>
  );
};
export default Footer;
