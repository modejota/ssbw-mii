import styles from '../page.module.css'

export default function AboveLayout({ children }) {
    return (
        <>
            <nav>
                <p style={{ marginLeft: '3vw' }}>Nav About</p>
            </nav>
            <main className={styles.main}>
                {children}
            </main>
        </>
    )
}