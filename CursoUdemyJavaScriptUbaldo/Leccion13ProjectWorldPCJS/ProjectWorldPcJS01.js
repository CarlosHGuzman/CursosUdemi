class DispositivoEntrada{
    constructor(tipoEntrada, marca){
        this._tipoEntrada = tipoEntrada;
        this._marca = marca;
    }

    get tipoEntrada(){
        return this._tipoEntrada;
    }
    set tipoEntrada(tipoEntrada){
        this._tipoEntrada = tipoEntrada;
    }

    get marca(){
        return this._marca;
    }
    set marca(marca){
        this._marca = marca;
    }
}

class Raton extends DispositivoEntrada{
    static contadorRatones = 0;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }

    get idRaton(){
        return this._idRaton;
    }

    toString(){
        return `idRaton: ${this._idRaton} Tipo entrada: ${this._tipoEntrada} Marca: ${this._marca}`;
    }
}

class Teclado extends DispositivoEntrada{
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclados;
    }

    get idTeclado(){
        return this._idTeclado;
    }

    toString(){
        return `ìdTeclado ${this._idTeclado} Tipo entrada: ${this._tipoEntrada} Marca: ${this._marca}`;
    }
}

class Monitor{
    static contadorMonitores = 0;

    constructor(marca, tamaño){
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;
        this._tamaño = tamaño;
    }

    get idMonitor(){
        return this._idMonitor;
    }

    get marca(){
        return this._marca;
    }
    set marca(marca){
        this._marca = marca;
    }

    get tamaño(){
        return this._tamaño;
    }
    set tamaño(tamaño){
        this._tamaño = tamaño;
    }

    toString(){
        return `idMonitor: ${this._idMonitor} Marca: ${this._marca} Tamaño: ${this._tamaño}`;
    }
}

class Computadora{
    static contadorComputadoras = 0;

    constructor(nombre, monitor, teclado, raton){
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._teclado = teclado;
        this._raton = raton;
    }

    get idComputadora(){
        return this._idComputadora;
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get monitor(){
        return this._monitor.toString();
    }
    set monitor(monitor){
        this._monitor = monitor;
    }

    get teclado(){
        return this._teclado.toString();
    }
    set teclado(teclado){
        this._teclado = teclado;
    }

    get raton(){
        return this._raton.toString();
    }
    set raton(raton){
        this._raton = raton;
    }

    toString(){
return `idComputadora: ${this._idComputadora} Nombre: ${this._nombre}\n\t Monitor: ${this.monitor}\n\t Teclado: ${this.teclado}\n\t Raton: ${this.raton}`;
    }
}

class Orden{
    static contadorOrdenes = 0;

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = [];
    }

    agregarComputadora(computadora){
        this._computadoras.push(computadora);
    }

    mostrarOrden(){
        let concatenarComputadoras = "";
        for(let computadora of this._computadoras){
            concatenarComputadoras += "\n" + computadora.toString();
        }
        console.log(`Orden: ${this._idOrden}, Computadoras: ${concatenarComputadoras}`);
    }
}

let monitor1 = new Monitor("HP", 15);
let raton1 = new Raton("USB", "Hp");
let teclado1 = new Teclado("Bluetooth", "MSI");
let computadora1 = new Computadora("HP", monitor1, teclado1, raton1);

let monitor2 = new Monitor("HP", 15);
let raton2 = new Raton("USB", "Hp");
let teclado2 = new Teclado("Bluetooth", "MSI");
let computadora2 = new Computadora("GAMER", monitor2, teclado2, raton2);
let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden();