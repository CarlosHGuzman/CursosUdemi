function miFuncion1(){
    console.log("Funcion 1");
}

function miFuncion2(){
    console.log("funcion 2");
}
/*callback = Llamar una funcion dentro de una funcion*/

function imprimir(mensaje){
    console.log(mensaje);
}

let imp = function imprimir(mensaje){
    console.log(mensaje);
}


function sumar(op1, op2, funcionCallBack){
    let res = op1 + op2;
    funcionCallBack(`Resultado: ${res}`);
}

sumar(5, 3, imprimir);
sumar(8, 5, imp);