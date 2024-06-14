import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const Register: React.FC = () => {
  const [username, setUsername] = useState<string>('')
  const [password, setPassword] = useState<string>('')
  const [role, setRole] = useState<string>('')
  const [message, setMessage] = useState<string>('')
  const navigate = useNavigate()

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    try {
      await axios.post('http://localhost:5000/api/register', { username, password, role })
      setMessage('User created successfully')
      navigate('/login')
    } catch (error) {
      setMessage('Error creating user')
    }
  }

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
        <input type="text" value={role} onChange={(e) => setRole(e.target.value)} placeholder="Role" required />
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  )
}

export default Register
