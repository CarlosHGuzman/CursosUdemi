package manejoexcepcionesP5.aritmetica;

import manejoexcepcionesP5.excepciones.OperacionExcepcion;

public class Aritmetica {
    //Como es de tipo RuntimeException no va ser necesario especificar de que clase vamos a trabajar la excepcion
    public static int division(int numerador, int denominador){
        if(denominador == 0){
            throw new OperacionExcepcion("Division entre cero"); 
        //se debe de colocar throw para que lo valide de que va arrojar una excepcion
        }
        return numerador/denominador;
    }
}
