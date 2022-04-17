package mx.com.gm.peliculas.negocio;

public interface ICatalogoPeliculas {
    
    public void agregarPelicula(String nombrePelicula, String nombreArchivo);
    
    public void listarPelicula(String nombreArchivo);
    
    public void buscarPelicula(String nombreArchivo, String buscar);
    
    public void iniciarCatalogoPeliculas(String nombreArchivo);
}