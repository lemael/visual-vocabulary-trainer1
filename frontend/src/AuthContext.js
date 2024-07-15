import React, { createContext, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState("");
  const [role, setRole] = useState("");

  const login = (name, userRole) => {
    setIsAuthenticated(true);
    setUsername(name);
    setRole(userRole);
  };

  const logout = () => {
    setIsAuthenticated(false);
    setUsername("");
    setRole("");
  };

  return (
    <AuthContext.Provider
      value={{ isAuthenticated, username, role, login, logout }}
    >
      {children}
    </AuthContext.Provider>
  );
};
