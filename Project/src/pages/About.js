import React from 'react';
import photo2 from "../assets/photo2.webp";
import photo3 from "../assets/photo3.webp";
import aboutphoto from "../assets/aboutphoto.jpg";

const About = () => {
  return (
    <div className="container mx-auto px-4">
      <div className="flex justify-center items-center mt-8">
        <img src={photo2} alt="Image1" className="shadow-lg hover:shadow-xl rounded-lg" />
      </div>
      <div className="text-center mt-8">
        <h1 className="text-4xl font-bold text-yellow-800">Hope Is Where the Heart Is</h1>
        <p className="mt-4 text-lg bg-yellow-200 p-4 rounded-lg">
          Canasu Dream Foundation is a non-governmental organization that empowers women through effective educational and livelihood initiatives.
        </p>
      </div>
      <div className="flex justify-center items-center mt-8">
        <img src={photo3} alt="Image12" className="shadow-lg hover:shadow-xl rounded-lg" />
      </div>
      <div className="text-center mt-8">
        <h2 className="text-2xl font-bold text-yellow-800">VISION</h2>
        <p className="mt-4 text-lg bg-yellow-200 p-4 rounded-lg">
          Our vision is to create a world in which all women determine the course of their lives & reach their full potential.
        </p>
      </div>
      <div className="text-center mt-8">
        <h2 className="text-2xl font-bold text-yellow-800">MISSION</h2>
        <div className="mt-4 text-lg bg-yellow-200 p-4 rounded-lg">
          Our mission is to support women to achieve their full potential; to encourage, enable and facilitate their active involvement in business, employment, learning and community life. We seek to achieve this by harnessing the economic power of women and communities, promoting education, skill development, social inclusion, and changing perceptions.
        </div>
      </div>
      <div className="text-center mt-8">
        <p className="text-lg bg-yellow-200 p-4 rounded-lg">
          We are a social community that is focused on helping women and assisting them in achieving their ambitions. We help them build and nurture their lives by providing skill sets that can help them accomplish their dreams and create an impact in their community. We also focus on providing training and hosting exhibitions which involve women learning to adapt to new opportunities. Canasu reaches out to communities around Bangalore and tries to emancipate women. We believe that if we strengthen the inner voice of women, they can nurture a community of achievers. To strengthen their inner voice, we need to strengthen their minds so that their determination propels them further.
        </p>
      </div>
      <div className="flex justify-center items-center mt-8">
        <img src={aboutphoto} alt="Image34" className="shadow-lg hover:shadow-xl rounded-lg" />
      </div>
      <div className="text-center mt-8">
        <h1 className="text-4xl font-bold text-yellow-800">OUR BELIEF</h1>
        <p className="mt-4 text-lg bg-yellow-200 p-4 rounded-lg">
          Canasu is not just an organization that helps women entrepreneurs, it is a revolution to support the dream of every woman to construct their future with perseverance. We strengthen their inner voice by driving away their fear of suppression and by bringing freedom into every sphere of their lives. We strongly believe that if we need to make the world a better place for tomorrow, women need to be architects of the future. There are several women in communities who are suppressed and are not supported due to social inequality and societal shackles. Our aim is to educate them and free them from this caged thinking which is hampering their growth.
        </p>
      </div>
    </div>
  );
};

export default About;
