'use client'

import { useState } from 'react'

export default function SocialSection() {
  const [copied, setCopied] = useState(false)

  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="mt-16 border-t border-gray-800 pt-12">
      {/* Social Links */}
      <div className="bg-gray-900 p-6 rounded-lg mb-8 border-l-4 border-yellow-500">
        <p className="text-gray-300 mb-2">
          <span className="text-yellow-500 font-bold">Tiktok:</span>
          <span className="text-blue-400 ml-2">@Appcheon.official</span>
        </p>
        <p className="text-gray-300 mb-2">
          <span className="text-yellow-500 font-bold">Beli Akses Web clone</span>
          <span className="text-blue-400 ml-2">(Modul)</span>
          <span className="text-yellow-500 ml-2">hanya di :</span>
          <a href="#" className="text-blue-400 ml-2 hover:underline">
            https://lynk.id/miyata
          </a>
        </p>
        <p className="text-gray-300 mb-2">
          <span className="text-yellow-500 font-bold">Beli All Mirror:</span>
          <a href="#" className="text-blue-400 ml-2 hover:underline">
            Appcheon.com
          </a>
        </p>
        <p className="text-gray-300">
          <span className="text-yellow-500 font-bold">Join Discord:</span>
          <button
            onClick={() => copyToClipboard('https://discord.gg/appcheon')}
            className="text-blue-400 ml-2 hover:underline"
          >
            {copied ? 'Copied!' : 'Klik Join discord'}
          </button>
        </p>
      </div>

      {/* Warning Section */}
      <div className="bg-yellow-900/30 border border-yellow-700 p-6 rounded-lg mb-8">
        <p className="text-yellow-300 text-sm">
          <span className="font-bold">⚠️ WAJIB BACA!</span>
          <span className="block mt-2">
            Saat kalian membeli akses maka admin akan meng-invite email milik kalian sendiri
            untuk diberikan akses,Maka kalian tidak boleh membagikan produk kita ,Harap Laporkan
            aenilahnya dan kalian akan mendapat Reward secara GRATIS! yaitu :
          </span>
          <span className="block mt-2">- Akses Web LIFETIME</span>
          <span className="block">- Membership AC 1 Bulan</span>
        </p>
      </div>

      {/* Footer */}
      <div className="flex items-center justify-center gap-2 text-gray-500 pt-8 border-t border-gray-800">
        <span>🍊</span>
        <span className="text-sm">Made with Super</span>
      </div>
    </div>
  )
}
