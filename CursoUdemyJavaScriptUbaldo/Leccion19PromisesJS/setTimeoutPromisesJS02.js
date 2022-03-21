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
    console.log("Inicio promesa");
    setTimeout(() => resolved("Saludos con promesa y timeout"), 3000);
    console.log("Fin promesa")
});


promesa.then(valor => console.log(valor));