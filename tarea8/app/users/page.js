import getAllUsers from "@/lib/getAllUsers"
import Link from 'next/link'

export const metadata = {
    title: 'Users',
    description: 'Apartado de usuarios',
}

export default async function UsersPage() {
    const userData = getAllUsers()
    const users = await userData

    const content = (
        <>
            <section>
                { users.map(user => {
                        return (
                            <p key={user.id} style={{ marginBottom: '8px', textAlign: 'center' }}>
                                <Link href={`/users/${user.id}`}>{user.name}</Link>
                            </p>
                        )
                    })
                }
            </section>
            <Link href="/">Link to Home</Link>
        </>
    )
    return content
}