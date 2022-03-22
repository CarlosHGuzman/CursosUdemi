package manejoexcepcionesP1.test;

import javax.swing.JOptionPane;

public class TestExcepciones {
    public static void main(String[] args){
        int resultado = 0; //se declara por fuera para que la podamos utilizar fuera del bloque try catch
        try{
            resultado = 10/0;
        }catch(Exception e){ //Exception variable que va almacenar nuestro error ya que arroja un String
            JOptionPane.showMessageDialog(null, "Ocurrio un error inesperado", "Error", 0);
            e.printStackTrace(System.out); //printStackTrace lo que hace es imprimir la pila de exceciones o fila
        }
        JOptionPane.showMessageDialog(null, "Division entre 0: " + resultado);
    }
}
