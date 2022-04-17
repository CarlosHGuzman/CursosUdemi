package ManejoArchivosP5.test;

import static ManejoArchivosP5.ManejoArchivos.leerArchivo;

public class TestManejoArchivo {
    public static void main(String[] args){
        //Tambien se puede dar la ruta en especifico en donde vamos a guardar el proyecto.
        //para ello debemos de acceder desde y colocando doble diagonal inversa c:\\
        var nombreArchivo = "C:\\Users\\carlo\\Documents\\CursosUdemi\\CursoUdemyJava\\ArchivosCreadosJava\\prueba.txt";
        //crearArchivo(nombreArchivo);
//        anexarArchivo(nombreArchivo, "Hola mi primer archivo");
        //escribirArchivo(nombreArchivo, "segunda linea");//Estamos sobre escribiendo la informacion que ya teniamos
//        anexarArchivo(nombreArchivo, "Segunda linea");
        leerArchivo(nombreArchivo);
    }
}
