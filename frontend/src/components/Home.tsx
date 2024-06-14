import React from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Home: React.FC = () => {
  const navigate = useNavigate()

  const handleLogout = async () => {
    await axios.post('http://localhost:5000/api/logout', {}, { withCredentials: true })
    navigate('/login')
  }

  return (
    <div>
      <h2>Welcome to Home</h2>
      <button onClick={handleLogout}>Logout</button>
    </div>
  )
}

export default Home
