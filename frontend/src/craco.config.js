const path = require("path");

module.exports = {
  webpack: {
    alias: {
      "@components": path.resolve(
        __dirname,
        "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/components/"
      ),
      "@pages": path.resolve(__dirname, "/src/components/pages/"),
      // Ajoutez d'autres alias ici
    },
  },
};
