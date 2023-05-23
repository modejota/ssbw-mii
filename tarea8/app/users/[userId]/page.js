import getUser from "@/lib/getUser"
import getUserPosts from "@/lib/getUserPosts"
import Link from "next/link"
import { Suspense } from "react"
import UserPosts from "./components/UserPosts"
import styles from "../../page.module.css"

export async function generateMetadata({ params: { userId } }) {
    // NextJS deduplicates the getUser() call
    const userData = getUser(userId);
    const user = await userData;

    return {
        title: user.name,
        description: `This is the page of ${user.name}`,
    };
}

export default async function UserPage({ params: { userId } }) {
    const userData = getUser(userId)
    const userPostsData = getUserPosts(userId)

    // Use Promise.all() to fetch data in parallel if not progressively rendering with Suspense
    // const [user, userPosts] = await Promise.all([userData, userPostsData])
    const user = await userData

    return (
        <>
            <h1>{user.name}</h1>
            <Suspense fallback={<h2>Loading...</h2>}>
                <UserPosts promise={userPostsData} />
            </Suspense>
            <div className={styles.mygrid}>
                <Link href="/">Link to Home</Link>
                <Link href="/users">Link to Users</Link>
            </div>
        </>
    )
}