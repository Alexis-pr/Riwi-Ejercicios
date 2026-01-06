
//alert("sincronizado correctamente");

// solicitud de datos
let nombre = prompt("¿Cuál es tu nombre?");
let edad = prompt("¿Cual es tu edad?");

// conversión de tipo a numero
edad = Number(edad);

// validación de entrada de edad
if (isNaN(edad)) {
    console.error("El valor ingresado no es un número válido.");
    edad = prompt("Por favor, ingresa un número válido para tu edad:");
}

// mensaje personalizado según la edad
if (edad < 18) {
   console.log("Hola " + nombre + ", eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!");
}else {
    console.log("Hola " + nombre + ", eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!");
}
//console.log(`hola a todos mi nombre es ${nombre} y tengo ${edad} años`)


// prueba en caso de recarga de página

/* reaload = confirm("¿Deseas recargar la página?");

if (reaload) {
    location.reload();
} else {
    console.log("Has decidido no recargar la página. ¡Continúa explorando!");
} */