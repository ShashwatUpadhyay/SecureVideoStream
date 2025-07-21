import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { Route, Routes, useLocation } from "react-router-dom";
import './App.css'
import VideoPlayer from './components/video.jsx'

function App() {
  const [count, setCount] = useState(0)

   return (
    <>
      <Routes>
        <Route path="/" element={<VideoPlayer />} />
      </Routes>
    </>
  )
}

export default App
