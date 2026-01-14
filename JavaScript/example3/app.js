const btnCambiarColor = document.getElementById('changeColor');
const titulo = document.getElementById('title');


btnCambiarColor.addEventListener('click', () => {
    titulo.style.color = titulo.style.color === 'blue' ? 'black' : 'blue';
});

const btnCambiarTexto = document.getElementById('changeTextBtn');

btnCambiarTexto.addEventListener('click', () => {
    titulo.textContent = titulo.textContent === 'Hello, World!' ? 'Text Changed!!!!' : 'Hello, World!';
}); 