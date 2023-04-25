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

                    // Creamos el cuerpo (tbody) para la tabla
                    var cuerpoTabla = document.createElement("tbody");
                    tabla.appendChild(cuerpoTabla);
                }
                // Actualizamos referencia a la tabla y la poblamos
                tablaResultadoLibros = document.getElementById("tabla_libros");
                tablaResultadoLibros.innerHTML = `
                    <thead>
                        <tr>
                            <th scope="col">ISBN</th>
                            <th scope="col">Título</th>
                            <th scope="col">Autor</th>
                            <th scope="col"></th>
                        </tr>
                    </thead>`;
                // Seleccionamos el cuerpo de la tabla
                var cuerpoTabla = tablaResultadoLibros.querySelector("tbody");

                libros.forEach(function (libro) {
                    // Creamos una fila para el cuerpo
                    var fila = document.createElement("tr");
                    // Creamos celdas para la fila
                    var celdaISBN = document.createElement("td");
                    celdaISBN.innerHTML = libro.isbn;
                    var celdaTitulo = document.createElement("td");
                    celdaTitulo.innerHTML = libro.title;
                    var celdaAutor = document.createElement("td");
                    celdaAutor.innerHTML = libro.author;
                    var celdaBoton = document.createElement("td");
                    var botonDetalle = document.createElement("a");
                    botonDetalle.href = "detalle/" + libro.isbn;
                    botonDetalle.classList.add("btn", "btn-primary");
                    botonDetalle.innerHTML = "Ver detalles";
                    celdaBoton.appendChild(botonDetalle);

                    // Agregamos las celdas a la fila
                    fila.appendChild(celdaISBN);
                    fila.appendChild(celdaTitulo);
                    fila.appendChild(celdaAutor);
                    fila.appendChild(celdaBoton);
                    // Agregamos la fila al cuerpo de la tabla
                    cuerpoTabla.appendChild(fila);
                });
            } else {
                // Si no hay resultados, vacio la tabla, creo el mensaje correspondiente y lo muestro.
                // Si ya tenemos un mensaje de "no hay resultados" no lo creamos de nuevo, sino que lo actualizamos
                tablaResultadoLibros.innerHTML = "";
                const container = document.getElementById("container_tabla_libros");
                const h1 = document.getElementById("no_resultados");
                if (!h1) {
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