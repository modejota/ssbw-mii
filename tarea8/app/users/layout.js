import styles from '../page.module.css'

export default function UsersLayout({ children }) {
    return (
        <>
            <main className={styles.main}>
                {children}
            </main>
        </>
    )
}