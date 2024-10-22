import { Route, Routes } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Dashboard from "./pages/Dashboard";
import About from "./pages/About";
import { useState } from "react";
import PrivateRoute from "./components/PrivateRoute";
import AdminDash from "./components/AdminDash";
import AdminMap from "./components/AdminMap"

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="w-screen min-h-screen flex flex-col">
      <Navbar isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />

      <Routes>
        <Route path="/" element={<Home isLoggedIn={isLoggedIn} />} />
        <Route path="/login" element={<Login setIsLoggedIn={setIsLoggedIn} />} />
        <Route path="/signup" element={<Signup setIsLoggedIn={setIsLoggedIn} />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute isLoggedIn={isLoggedIn}>
              <Dashboard />     
            </PrivateRoute>
          }
        />
        <Route path="/adminmap" element={<AdminMap />} />
      </Routes>
    </div>
  );
}

export default App;
