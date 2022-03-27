package ManejoArchivosP3;

//io = input, output
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class ManejoArchivos {

    public static void crearArchivo(String nombreArchivo) {
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
            salida.close(); //Para terminar de crearlo se debe de cerrar
        }
    }

    public static void escribirArchivo(String nombreArchivo, String contenido) {
        PrintWriter salida = null;
        try {
            File archivo = new File(nombreArchivo);
            salida = new PrintWriter(archivo);
            salida.println(contenido);
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
        } finally {
            System.out.println("Se ha escrito el archivo");
            salida.close();
        }
    }
}
