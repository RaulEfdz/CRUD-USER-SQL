import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import App from './App.tsx'

import './index.css'
import Login from './components/Login.tsx'
import Register from './components/Register.tsx'
import Home from './components/Home.tsx'

ReactDOM.createRoot(document.getElementById('root')as Element).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </Router>
  </React.StrictMode>
)
