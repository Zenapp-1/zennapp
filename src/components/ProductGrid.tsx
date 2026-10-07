'use client'

import { useState } from 'react'

interface ProductCard {
  id: number
  title: string
  image: string
  alt: string
}

export default function ProductGrid() {
  const [products] = useState<ProductCard[]>([
    {
      id: 1,
      title: 'Akademi Crypto',
      image: 'https://via.placeholder.com/300x200?text=Akademi+Crypto',
      alt: 'Akademi Crypto',
    },
    {
      id: 2,
      title: 'Trade with Suli',
      image: 'https://via.placeholder.com/300x200?text=Trade+with+Suli',
      alt: 'Trade with Suli',
    },
    {
      id: 3,
      title: 'Ternak Uang',
      image: 'https://via.placeholder.com/300x200?text=Ternak+Uang',
      alt: 'Ternak Uang',
    },
  ])

  return (
    <div className="w-full">
      <h2 className="text-xl font-semibold mb-6 text-gray-400 flex items-center gap-2">
        <span className="text-gray-600">⊞</span>
        AppCheon Webclone
      </h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {products.map((product) => (
          <div
            key={product.id}
            className="bg-black rounded-lg overflow-hidden hover:scale-105 transition-transform duration-300 cursor-pointer"
          >
            <div className="relative w-full aspect-square bg-black">
              <img
                src={product.image}
                alt={product.alt}
                className="w-full h-full object-contain p-2"
                style={{ maxHeight: '200px' }}
              />
            </div>
            <div className="p-4 bg-gray-900">
              <p className="text-center text-gray-400 text-sm flex items-center justify-center gap-2">
                <span className="text-green-400">◐</span>
                {product.title}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
