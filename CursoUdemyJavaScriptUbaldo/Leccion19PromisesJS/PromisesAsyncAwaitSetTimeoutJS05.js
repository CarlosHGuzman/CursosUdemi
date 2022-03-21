/*let nombre = new Promise((resolver, rechazar)); */
let miPromesa = new Promise((resolved, rejected) =>{
    let expresion = true;
    if(expresion)
        resolved('Resolvió correcto')
    else
        rejected("Se produjo un error")
})

// miPromesa.then(
//     valor =>console.log(valor),
//     error => console.log(error)
// )

// miPromesa.then(valor => console.log(valor))//En caso de que haya salido exitosamente
// .catch(error => console.log(error));//en caso de que haya salido mal 

let promesa = new Promise((resolved) =>{
    // console.log("Inicio promesa");
    setTimeout(() => resolved("Saludos con promesa y timeout"), 3000);
//   console.log("Fin promesa");
});


// promesa.then(valor => console.log(valor));

// async indica que una funcion va a regresar una promesa
async function miFuncionConPromesa(){
    return "saludos con promesa y async"
}

// miFuncionConPromesa().then(valor => console.log(valor));

async function funcionConPromesaYAwait(){
    let miPromesa = new promesa((resolved) => {
        resolved("Promesa con await");
    });
    // await solo se puede usar dentro de una funcion declarada con async
    console.log(await miPromesa);
}

//funcionConPromesaYAwait();

//promesas, await, async y setTimeout
async function funcionConPromesaAwaitTimeout(){
    console.log("Inicio funcion");
    let miPromesa = new Promise(resolver => {
        setTimeout(() => {resolver("Promesa con await y timeout")},10000);
    });
    console.log(await miPromesa);
    console.log("Fin funcion");
}
funcionConPromesaAwaitTimeout();