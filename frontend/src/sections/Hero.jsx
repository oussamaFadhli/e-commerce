import React, { useState, useEffect } from "react";
import {
  SliderImage1,
  SliderImage2,
  SliderImage3,
  SliderImage4,
  SliderImage5,
} from "../assets";
import { Link } from "react-router-dom";
import NavigateNextIcon from '@mui/icons-material/NavigateNext';
import NavigateBeforeIcon from '@mui/icons-material/NavigateBefore';

const Hero = () => {
  const photos = [
    SliderImage1,
    SliderImage2,
    SliderImage3,
    SliderImage4,
    SliderImage5,
  ];
  const [currentSlide, setCurrentSlide] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentSlide((currentSlide + 1) % photos.length);
    }, 5000);

    return () => clearInterval(intervalId);
  }, [currentSlide, photos.length]);

  const handleNextSlide = () => {
    setCurrentSlide(currentSlide === photos.length - 1 ? 0 : currentSlide + 1);
  };

  const handlePrevSlide = () => {
    setCurrentSlide(currentSlide === 0 ? photos.length - 1 : currentSlide - 1);
  };

  return (
    <section className="bg-white">
      <div className="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 gap-8">
        <div className="mr-auto place-self-center lg:col-span-7">
          <h1 className="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl text-[#1B5A7D]">
            Canon camera
          </h1>
          <Link
            to="#"
            className="inline-flex items-center justify-center px-5 py-3 mr-3 text-base font-medium text-center text-white rounded-lg bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 bg-[#EDA415]"
          >
            Shop now
            <svg
              className="w-5 h-5 ml-2 -mr-1"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"></path>
            </svg>
          </Link>
          <Link
            to="#"
            className="inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-[#316887] border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:ring-gray-100"
          >
            View more
          </Link>
        </div>
        <div className="lg:mt-0 lg:col-span-5 lg:flex">
          <img
            src={photos[currentSlide]}
            alt={`Slide ${currentSlide}`}
            className="animate-fade-in w-96 h-96"
          />
          <div className="absolute top-1/2 left-4 transform -translate-y-1/2">
            <button
              onClick={handlePrevSlide}
              className="p-3 bg-gray-200 rounded-full focus:outline-none"
            >
              <NavigateBeforeIcon />
              <span className="sr-only">Previous slide</span>
            </button>
          </div>
          <div className="absolute top-1/2 right-4 transform -translate-y-1/2">
            <button
              onClick={handleNextSlide}
              className="p-3 bg-gray-200 rounded-full focus:outline-none"
            >
              <NavigateNextIcon />
              <span className="sr-only">Next slide</span>
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
