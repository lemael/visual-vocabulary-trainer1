import "./App.css";
import { AuthProvider } from "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/AuthContext";
import Footer from "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/components/layout/footer/Footer";
import Header from "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/components/layout/header/Header";
import HomePage from "/home/mael/Dokumente/visual-vocabulary-trainer1/frontend/src/components/pages/HomePage/HomePage";

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <Header />
        <HomePage />
        <Footer />
      </div>
    </AuthProvider>
  );
}

export default App;
