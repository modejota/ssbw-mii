import { useState, useEffect } from 'react'

const Dogs = () => {

    const [isLoading, setIsLoading] = useState(true);
    const [imageUrl, setImageUrl] = useState(null);

    useEffect(() => {
        if (isLoading) {
            fetch("https://dog.ceo/api/breeds/image/random")
                .then((response) => response.json())
                .then((dog) => {
                    setImageUrl(dog.message);
                    setIsLoading(false);
                });
        }
    }, [isLoading]);

    const randomDog = () => {
        setIsLoading(true);
    };

    if (isLoading) {
        return (
            <div className="DogContainer" style={{ margin: 'auto', textAlign: 'center' }}>
                <h1>Cargando...</h1>
            </div>
        );
    }

    return (
        <div className="DogContainer" style={{ margin: 'auto', textAlign: 'center' }}>
            <img src={imageUrl} alt="Imagen de perrito aleatoria" style={{ maxWidth: '100%', maxHeight: '100%' }} />
            <div style={{ marginTop: '0.4vh' }}>
                <button onClick={randomDog}> ¡Otro!{" "}
                    <span role="img" aria-label="corazón">❤️</span>
                </button>
            </div>
        </div>
    );

}

export default Dogs