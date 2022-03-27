package ManejoArchivosP3.test;

import static ManejoArchivosP1.ManejoArchivos.crearArchivo;
import static ManejoArchivosP3.ManejoArchivos.escribirArchivo;

public class TestManejoArchivo {
    public static void main(String[] args){
        //Tambien se puede dar la ruta en especifico en donde vamos a guardar el proyecto.
        //para ello debemos de acceder desde y colocando doble diagonal inversa c:\\
        var nombreArchivo = "C:\\Users\\carlo\\Documents\\CursosUdemi\\CursoUdemyJava\\ArchivosCreadosJava\\prueba.txt";
        //crearArchivo(nombreArchivo);
        escribirArchivo(nombreArchivo, "Hola mi primer archivo");
    }
}
