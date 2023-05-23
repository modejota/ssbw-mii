export default async function UsersPosts({promise}) {
    const posts = await promise
    const content = (
        <>
            <section>
                { posts.map(post => {
                        return (
                            <>
                            <article key={post.id} style={{ textAlign: 'center' }} >
                              <h2>{post.title}</h2>
                              <p>{post.body}</p>
                              <br />
                            </article></>
                        )
                    })
                }
            </section>
        </>
    )
    return content
}
