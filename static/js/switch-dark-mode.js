function changeModeImage() {
    const htmlFather = document.querySelector('html')
    const imgButton = document.querySelector('#img-darkmode-button')
    if (htmlFather.classList.contains('dark')) {
        imgButton.src = "/static/images/sol.png"
    } else {
        imgButton.src = "/static/images/luna.png"
    }
}
// Espear a que se cargue el DOM ya que consultamos la etiqueta HTML raiz, no basta con poner script al final
window.addEventListener('DOMContentLoaded', () => {
    changeModeImage()
});
// Cambiar a modo oscuro y el icono del boton
document.querySelector("#darkmode-button").onclick = function (e) {
    darkmode.toggleDarkMode();
    changeModeImage();
}