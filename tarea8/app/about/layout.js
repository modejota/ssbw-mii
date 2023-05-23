import styles from '../page.module.css'

export default function AboveLayout({ children }) {
    return (
        <>
            <nav>Nav About</nav>
            <main className={styles.main}>
                {children}
            </main>
        </>
    )
}