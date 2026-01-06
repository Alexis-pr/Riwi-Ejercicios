
// Punto 1
let nombre = prompt("¿Cuál es tu nombre?");
let edad = Number(prompt("¿Cuántos años tienes?"));
let correo = prompt("¿Cuál es tu correo electrónico?");

let estado = prompt("¿Estás activo? (true/false)").toLowerCase();
//estado = Boolean(estado) // Convertir edad a booleano
estado = estado === "true";
//ingresoDatos();    
console.group("Tipos de Datos del usuario:");
console.log(typeof nombre + " " + nombre); // string
console.log(typeof edad + " " + edad);   // number  
console.log(typeof correo + " " + correo) ; // string
console.log(typeof estado + " " +  estado); // boolean
console.groupEnd();



// Punto 2
console.group("Validación de Edad:");
validarEdad(edad);

//&& estado != false || estado != 0 || estado != null || estado != undefined || estado != NaN
if (nombre != "" && estado == true) {       
    console.log("Usuario activo con nombre registrado.");    
}else{
     console.log("Usuario con estado inactivo o sin nombre registrado.");
}

console.groupEnd();

// Punto 3

contraseñaIngresada= prompt("Por favor, ingresa una contraseña (mínimo 8 caracteres):");
intento = 0;

console.group("Validación de Contraseña:");
validarContraseña(contraseñaIngresada , intento);

console.groupEnd();

// Punto 4 -- funciones

/* function ingresoDatos() {
    let nombre = prompt("¿Cuál es tu nombre?");
    let edad = Number(prompt("¿Cuántos años tienes?"));
    let correo = prompt("¿Cuál es tu correo electrónico?");

    let estado = prompt("¿Estás activo? (true/false)").toLowerCase();
    // estado = Boolean(estado) // Convertir edad a booleano
    estado = estado === "true";
    
    console.log(typeof nombre + " " + nombre); // string
    console.log(typeof edad + " " + edad);   // number  
    console.log(typeof correo + " " + correo) ; // string
    console.log(typeof estado + " " +  estado); // boolean
    
    return console.log(` 
    El nombre del usuario es: ${nombre},
    La edad del usuario es: ${edad},
    El correo del usuario es: ${correo},
    El estado del usuario es: ${estado}.    
    `)

   
}
 */


function validarEdad(edad) {

    if (edad < 0 || isNaN(edad)) {
        console.error("Edad inválida. Por favor, ingresa una edad válida.");
    } else if (edad >= 18) {
        console.log("Es mayor de edad.");
    } else {
        console.warn("Es menor de edad.");
    }
}

function validarContraseña(contraseña , intento) {
    contraseñaGuardada = "Segura123";
    while (intento < 2 ) {
   
        if (contraseña === contraseñaGuardada) {
            // %c para dar estilo al mensaje en la consola
            console.log("%c Contraseña Correcta. Acceso concedido", "color: white ; background-color: green; font-size: 15px ; font: small-caps 100%/200% serif;");
            
            break;
        }else {
            console.log("%c Contraseña incorrecta. Intenta de nuevo.", "color: white ; background-color: red ; font-size: 15px ; font: small-caps 100%/200% serif;");
            
            contraseñaIngresada = prompt("Por favor, ingresa una contraseña (mínimo 8 caracteres):");
            contraseña = contraseñaIngresada; // actualiza la contraseña ingresa nuevamente para entrar en el siguiente ciclo
        }
        intento++;
        if (intento == 2) {
            console.log("%c Has agotado todos los intentos. Acceso denegado.", "color: white ; background-color: red;font-size: 15px ; font: small-caps 100%/200% serif;");  
            break;         
        }
    }      
}

