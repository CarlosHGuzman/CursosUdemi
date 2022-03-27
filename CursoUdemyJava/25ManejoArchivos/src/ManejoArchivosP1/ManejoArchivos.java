
package ManejoArchivosP1;

//io = input, output
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class ManejoArchivos {
    public static void crearArchivo(String nombreArchivo){
        PrintWriter salida = null;
        try {
            //Con esto solo hemos creado un objeto de tipo File en memoria
            File archivo = new File(nombreArchivo);
            //Aqui hay dos opciones o declaramos un bloque try catch para procesarla o nosotros 
            //Hacemos una clase para manejar la excepcion de tipo checkException
            salida = new PrintWriter(archivo);//Aqui solo hemos abierto el archivo
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
        } finally {
            System.out.println("Se creo el archivo");
            salida.close(); //Para terminar de crearlo se debe de cerrar
        }
    }
}
