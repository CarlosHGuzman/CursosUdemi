package ManejoArchivosP5;

//io = input, output
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
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

    public static void anexarArchivo(String nombreArchivo, String contenidoAnexar) {
        PrintWriter salida = null;
        try {
            File archivo = new File(nombreArchivo);
            //En vez de enviar directamente el objeto archivo vamos a mandar un argumento 
            //Este seria un objeto de tipo FileWriter el cual recibe dos argumentos
            //El primero seria el objeto archivo y el segundo un booleanos para ver si se va a sobreescribir
            //El contenido
            salida = new PrintWriter(new FileWriter(archivo, true));
            salida.println(contenidoAnexar);
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
        } catch (IOException ex) {
            ex.printStackTrace(System.out);
        } finally {
            System.out.println("Se ha Anexado la informacion");
            salida.close();
        }
    }

    public static void leerArchivo(String nombreArchivo) {
        File archivo = new File(nombreArchivo);
        //Podemos leer lineas completas del archivo
        //FileReader no lee lineas completas por eso utilizamos BufferedReader
        BufferedReader entrada = null;
        try {
            entrada = new BufferedReader(new FileReader(archivo));
            var lectura = entrada.readLine();//Esto solo nos devuelve una linea, asi que debemos de recorrerlo
            while (lectura != null) {//Mientras no lea una linea vacia
                System.out.println("Lecutra = " + lectura);
                lectura = entrada.readLine();
            }
            System.out.println("Termino la lectura");
            entrada.close();
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
        } catch (IOException ex) {
            ex.printStackTrace(System.out);
        }
    }
}
