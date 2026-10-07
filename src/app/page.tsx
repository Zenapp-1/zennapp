'use client'

import { useState } from 'react'
import ProductGrid from '@/components/ProductGrid'
import SocialSection from '@/components/SocialSection'
import Header from '@/components/Header'

export default function Home() {
  return (
    <main className="min-h-screen bg-dark">
      <Header />
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <ProductGrid />
        <SocialSection />
      </div>
    </main>
  )
}
