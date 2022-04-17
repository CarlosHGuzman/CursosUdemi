package mx.com.gm.peliculas.presentacion;

import javax.swing.JOptionPane;
import mx.com.gm.peliculas.negocio.*;

public class CatalogoPeliculasPresentacion {
    public static void main(String[] args) {
        String opcion = null;
        do{
            opcion = String.valueOf(JOptionPane.showInputDialog(null, "Elija una opcion", "Menu", JOptionPane.QUESTION_MESSAGE, null, new Object[]{"Iniciar catalogo peliculas"
            , "Agregar pelicula", "Listar peliculas", "Buscar pelicula", "Salir"}, "Salir"));
            ICatalogoPeliculas catalogo = new CatalogoPeliculasImp();
            switch(opcion){
                case "Iniciar catalogo peliculas": catalogo.iniciarCatalogoPeliculas("archivo.txt"); 
                break;
                case "Agregar pelicula": 
                    var nombre = JOptionPane.showInputDialog("Ingrese el nombre de la pelicula: ");
                    catalogo.agregarPelicula(nombre, "archivo.txt");
                    break;
                case "Listar peliculas": catalogo.listarPelicula("archivo.txt"); break;
                case "Buscar pelicula": 
                    var nombreBuscar = JOptionPane.showInputDialog("Ingrese el nombre de la pelicula: ");
                    catalogo.buscarPelicula("achivo.txt", nombreBuscar);
                    break;
                case "Salir": JOptionPane.showMessageDialog(null, "Hasta luego"); break;
                default: System.out.println("Error");
            }
        }while(!"Salir".equals(opcion));
    }
}
