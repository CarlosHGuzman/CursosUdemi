/*Manda a llamar a la funcion callback cada cierto tiempo que indiquemos*/

let reloj = () =>{
    let fecha = new Date(); // fecha actual
    if(fecha.getHours() === fecha.getHours() + 2){
        console.log("Alerta");
    }
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

setInterval(reloj, 1000); // 1 seg
