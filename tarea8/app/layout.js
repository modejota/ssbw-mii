import './globals.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Tarea 8 SSBW',
  description: 'Tarea 8 de la asignatura SSBW del Máster Ingenería Informática UGR',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav>
          <h1>My Navbar</h1>
        </nav>
        {children}
      </body>
    </html>
  )
}
