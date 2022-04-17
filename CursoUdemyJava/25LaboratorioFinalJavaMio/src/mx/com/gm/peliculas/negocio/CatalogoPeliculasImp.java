package mx.com.gm.peliculas.negocio;

import javax.swing.JOptionPane;
import mx.com.gm.peliculas.datos.AccesoDatosImpl;
import mx.com.gm.peliculas.datos.IAccesoDatos;
import mx.com.gm.peliculas.domain.Pelicula;
import mx.com.gm.peliculas.excepciones.AccesoDatosEx;
import mx.com.gm.peliculas.excepciones.LecturaDatosEx;

public class CatalogoPeliculasImp implements ICatalogoPeliculas{
    
    private final IAccesoDatos datos;
    
    public CatalogoPeliculasImp(){
        this.datos = new AccesoDatosImpl();
    }
    
    @Override
    public void agregarPelicula(String nombrePelicula, String nombreArchivo) {
        try {
            Pelicula pelicula = new Pelicula(nombrePelicula);
            boolean anexar = false;
            anexar = datos.existe();
            datos.escribir(pelicula, anexar);
        } catch (AccesoDatosEx ex) {
            ex.printStackTrace(System.out);
            System.out.println("Error de acceso a datos");
        }
    }

    @Override
    public void listarPelicula(String nombreArchivo) {
        String unir = "";
        try {
            var peliculas = this.datos.listar();
            for(var pelicula: peliculas){
                unir += "Pelicula: " + pelicula +"\n";
            }
            JOptionPane.showMessageDialog(null, unir, "Peliculas listadas", 1);
        } catch (AccesoDatosEx ex) {
            ex.printStackTrace(System.out);
            System.out.println("Error de acceso de datos");
        }
    }

    @Override
    public void buscarPelicula(String nombreArchivo, String buscar) {
        String resultado = null;
        try {
            resultado = this.datos.buscar(buscar);
        } catch (LecturaDatosEx ex) {
            ex.printStackTrace(System.out);
            System.out.println("Error de lectura de datos");
        }
        JOptionPane.showMessageDialog(null, "Pelicula: " + resultado, "Pelicula encontrada", 1);
    }

    @Override
    public void iniciarCatalogoPeliculas(String nombreArchivo) {
        try {
            if(this.datos.existe()){
                datos.borrar();
                datos.crear(nombreArchivo);
            }else{
                datos.crear(nombreArchivo);
            }
        } catch (AccesoDatosEx ex) {
            ex.printStackTrace(System.out);
            System.out.println("Error al iniciar catalogo peliculas");
        }
    }

}
