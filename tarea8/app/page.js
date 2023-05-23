import styles from './page.module.css'
import Link from 'next/link'
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <main className={styles.main}>
      <h1 className={styles.title}>Hello World!</h1>
      <div className={styles.mygrid}>
        <Link href="/about">Link to About</Link>
        <Link href="/users">Link to Users</Link>
      </div>
    </main>
  )
}
