package manejoexcepcionesP3.aritmetica;

import manejoexcepcionesP3.excepciones.OperacionExcepcion;

public class Aritmetica {
    //se debe de colocar throws y la clase de la que hereda para hacerle saber de que posiblemente
    //va arrojar una excepcion, y que para el manejo vamos a utilizar esa clase
    public static int division(int numerador, int denominador) throws OperacionExcepcion{
        if(denominador == 0){
            throw new OperacionExcepcion("Division entre cero"); 
        //se debe de colocar throw para que lo valide de que va arrojar una excepcion
        }
        return numerador/denominador;
    }
}
