import { useState } from 'react'
import Header from './components/Header'
import Mainsite from './components/Mainsite'
import './App.css'
import Checker from './components/Checker'
import Footer from './components/Footer'

function App() {

  return (
    <>
  <div className='flex flex-col justify-fill m-0 p-0 gap-0 bg-gray-900'>
      
      <Header />       
      <Mainsite />
      <Checker />
      <Footer />
  </div>
    </>
  )
}

export default App
