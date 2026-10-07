import type { Metadata } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: "AppCheon - Upgrade your skill",
  description: "Learn and upgrade your skills with AppCheon",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-dark text-white font-sans">{children}</body>
    </html>
  )
}
