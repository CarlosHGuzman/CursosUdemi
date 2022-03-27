package ManejoGenericsP2.test;

import ManejoGenericsP1.genericos.ClaseGenerica;
import javax.swing.JOptionPane;

public class TestGenerics {
    public static void main(String[] args){
        //Nosotros utilizamos la notacion de diamante para indicar el tipo pero esto no es necesario 
        //La clase que creamos puede inferir el tipo
        ClaseGenerica<Integer> objetoInt = new ClaseGenerica(15);
        objetoInt.obtenerTipo();
        
        //Debemos de utilizar tipos que sean compatibles, es decir, podemos utilizar en la notacion de diamante
        //Una clase y en el envio del argumento una clase hija o una interface y como valor un tipo que la halla implementado
        ClaseGenerica<String> objetoString = new ClaseGenerica("MIlaneso");
        objetoString.obtenerTipo();
    }
}
