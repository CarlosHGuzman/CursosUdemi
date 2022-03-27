package ManejoArchivosP2.test;

import static ManejoArchivosP1.ManejoArchivos.crearArchivo;

public class TestManejoArchivo {
    public static void main(String[] args){
        //Tambien se puede dar la ruta en especifico en donde vamos a guardar el proyecto.
        //para ello debemos de acceder desde y colocando doble diagonal inversa c:\\
        var nombreArchivo = "prueba.txt";
        crearArchivo(nombreArchivo);
    }
}
