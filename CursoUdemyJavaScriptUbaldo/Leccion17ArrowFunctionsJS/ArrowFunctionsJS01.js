"use strict";
function miFuncion(){ // Normal
    console.log("Saludos desde mi funcion");
}
let miFuncionDos = function(){ // Tipo Expresion
    console.log("Saludos desde mi funcion dos");
}

const miFuncionFlecha = () =>{ // no aplica concepto hoisting
    console.log("Saludos desde mi funcion flecha");
}

miFuncion();
miFuncionFlecha();