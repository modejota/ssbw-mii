const inputFieldBuscadorLibros = document.getElementById("input_buscador");
let tablaResultadoLibros = document.getElementById("tabla_libros");
const formularioBuscarLibros = document.getElementById("formulario_buscar_libros");
const botonBuscadorLibros = document.getElementById("boton_buscar_libro");

// En la página principal evitamos que se envíe el formulario ya que desactivamos
// el "envío automático" al pulsar ENTER y nos deshacemos del botón de enviar. Forzamos uso de JavaScript.
// En otras páginas como la de "añadir libro" o "editar libro" sí que queremos que se envíe el formulario
formularioBuscarLibros.addEventListener('submit', function (e) {
    e.preventDefault();
})
if (botonBuscadorLibros)
    botonBuscadorLibros.remove()

inputFieldBuscadorLibros.addEventListener('input', function () {
    axios.get('/busqueda_reactiva/libros?search=' + inputFieldBuscadorLibros.value)
        .then(function (response) {
            // Eliminamos posible mensaje de "no hay resultados" que sí viniera del formulario de búsqueda desde otra página
            const h1 = document.getElementById("no_resultados");
            if (h1)
                h1.remove();

            const libros = response.data.books
            if (libros.length != 0) {
                // Si venimos del formulario de búsqueda desde otra página, la tabla no existe, hay que crearla
                if (!tablaResultadoLibros) {
                    const container = document.getElementById("container_tabla_libros");
                    const tabla = document.createElement("table");
                    tabla.id = "tabla_libros";
                    tabla.classList.add("table", "mb-4")
                    tabla.style.tableLayout = "fixed";  // Siempre mismo ancho de columnas, independientemente del contenido
                    container.appendChild(tabla);
                }
                // Actualizamos referencia a la tabla y la poblamos
                tablaResultadoLibros = document.getElementById("tabla_libros");
                tablaResultadoLibros.innerHTML = "";
                tablaResultadoLibros.innerHTML += `
                    <thead>
                        <tr>
                            <th scope="col">ISBN</th>
                            <th scope="col">Título</th>
                            <th scope="col">Autor</th>
                            <th scope="col"></th>
                            </tr>
                    </thead>`
                libros.forEach(function (libro) {
                    tablaResultadoLibros.innerHTML += `
                        <tr>
                            <td>${libro.isbn}</td>
                            <td>${libro.title}</td>
                            <td>${libro.author}</td>
                            <td><a href="detalle/${libro.isbn}" class="btn btn-primary">Ver detalles</a></td>
                        </tr>
                    `;
                });
            } else {
                // Si no hay resultados, vacio la tabla, creo el mensaje correspondiente y lo muestro.
                // Si ya tenemos un mensaje de "no hay resultados" no lo creamos de nuevo, sino que lo actualizamos
                tablaResultadoLibros.innerHTML = "";
                const container = document.getElementById("container_tabla_libros");
                const h1 = document.getElementById("no_resultados");
                if(!h1) {
                    const h1Nuevo = document.createElement("h1");
                    h1Nuevo.id = "no_resultados";
                    h1Nuevo.classList.add("mb-4")
                    h1Nuevo.innerText = `No hay resultados para la búsqueda: ${inputFieldBuscadorLibros.value}`
                    container.appendChild(h1Nuevo);
                } else
                    h1.innerText = `No hay resultados para la búsqueda: ${inputFieldBuscadorLibros.value}`
            }
        })
        .catch(function (error) {
            console.log(error);
        });
})