"use strict";
function miFuncion(){ // Normal
    console.log("Saludos desde mi funcion");
}
let miFuncionDos = function(){ // Tipo Expresion
    console.log("Saludos desde mi funcion dos");
}

// const miFuncionFlecha = () =>{ // no aplica concepto hoisting
//     console.log("Saludos desde mi funcion flecha");
// }

// const miFuncionFlecha = () => console.log("Saludos desde mi funcion tipo flecha en la misma linea");

miFuncion();
// miFuncionFlecha();

// const saludar = () => {
//     return "Saludos desde mi funcion tipo flecha con return";
// }

const saludar = () => "Saludos desde mi funcion flecha sin return y sin console.log()";

console.log(saludar());

const regresaObjeto = () => ({nombre: "Carlos", apellido: "Guzman"})
console.log(regresaObjeto());

const funcionConParametros = (mensaje) => console.log(mensaje);
funcionConParametros("Saludos con parametros o argumentos");

const funcionConParametros2 = (mensaje) => {
    console.log(mensaje);
}
funcionConParametros2("Saludos con parametros o argumentos");

const funcionParametros = mensaje => console.log(mensaje); // Se puede omitir el uso de parentesis para el parametro si solo es uno
funcionParametros("yhoaljfdksalfjkñsdla");

const funcionConParametros3 = (op1, op2) => op1 + op2;
console.log(funcionConParametros3(3,5));


const funcionConVariosParametros = (op1, op2) => {
    let resultado = op1 + op2;
    return `Resultado ${resultado}`;
}

console.log(funcionConVariosParametros(3, 5));