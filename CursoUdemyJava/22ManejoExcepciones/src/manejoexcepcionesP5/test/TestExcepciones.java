package manejoexcepcionesP5.test;

import javax.swing.JOptionPane;
import manejoexcepcionesP5.aritmetica.Aritmetica;

public class TestExcepciones {

    public static void main(String[] args) {
        int resultado = 0;
        resultado = Aritmetica.division(10, 0); //como ya no es de tipo Exception ya no nos va a marcar el error
        //por ende se puede omitir el try catch, cuando hago referencia a marcar es a la linea roja que se coloca en el codigo

        //se suele utilizar RuntimeException cuando no es seguro que se arroje la excepcion para que quede mas limpuio el codigo
        //se suele utilizar Exception cuando se sabe que es muy probable que ocurra la excepcion
        
        JOptionPane.showMessageDialog(null, "Division entre 0: " + resultado);
    }
}
