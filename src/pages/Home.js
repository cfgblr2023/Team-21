import React from 'react'
import ImageSlider from '../components/ImageSlider';
import { SliderData } from '../components/SliderData';
const Home = () => {
  return (
    <div className='flex justify-center items-center text-white text-3xl h-full'>
      
          <ImageSlider slides={SliderData} />;
    </div>
  )
}

export default Home
