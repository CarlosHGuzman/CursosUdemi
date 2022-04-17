package manejoexcepcionesP6.test;

import javax.swing.JOptionPane;
import manejoexcepcionesP5.excepciones.OperacionExcepcion;
import manejoexcepcionesP5.aritmetica.Aritmetica;

public class TestExcepciones {

    public static void main(String[] args) {
        int resultado = 0; //se declara por fuera para que la podamos utilizar fuera del bloque try catch
        try{
            resultado = Aritmetica.division(10,0);
        }catch(OperacionExcepcion e){//se suele colocar las excepciones de menor jerarquia a mayor jerarquia para asi terminar con la clase Exception
            System.out.println("Ocurrio un error de tipo Operacion Exception: ");
            System.out.println(e.getMessage());
        }
        catch(Exception e){ //Exception variable que va almacenar nuestro error ya que arroja un String
            JOptionPane.showMessageDialog(null, "Ocurrio un error inesperado", "Error", 0);
            e.printStackTrace(System.out); //printStackTrace lo que hace es imprimir la pila de exceciones o fila
            JOptionPane.showMessageDialog(null, e.getMessage(), "Error", 0);
        }finally{ //El bloque finally siempre se va a ejecutar en el caso de que arroje o no excepcion
            //esto hace que el bloque finally se utilice para cerrar recursos como lo puede una conexion a una base de datos    
            System.out.println("se reviso la division entre 0");
        }
        
        JOptionPane.showMessageDialog(null, "Division entre 0: " + resultado);
    }
}
