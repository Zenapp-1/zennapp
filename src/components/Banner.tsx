import React from 'react';

interface BannerProps {
  title: string;
  description: string;
  backgroundImage?: string;
  className?: string;
}

export default function Banner({ 
  title, 
  description, 
  backgroundImage = '/default-banner.jpg',
  className = '' 
}: BannerProps) {
  const bannerStyle = {
    backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url(${backgroundImage})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    width: '100%',
    minHeight: '300px',
    display: 'flex',
    alignItems: 'center',
  };

  return (
    <div 
      className={`w-full mx-auto py-16 px-4 sm:px-6 lg:px-8 text-white ${className}`}
      style={bannerStyle}
    >
      <div className="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl md:text-4xl font-bold mb-3">{title}</h1>
        <p className="text-gray-200 text-lg">{description}</p>
      </div>
    </div>
  );
}
