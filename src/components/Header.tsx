'use client'

import Banner from './Banner'

export default function Header() {
  return (
    <div className="w-full">
      <Banner 
        title="Upgrade your Knowledge with ZEN APP"
        description="Tingkatkan wawasan dan keterampilan Anda dengan konten berkualitas tinggi"
        backgroundImage="/banner.jpg"
      />
    </div>
  )
}
