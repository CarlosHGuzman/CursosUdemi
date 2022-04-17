package mx.com.gm.peliculas.datos;

import java.util.List;
import mx.com.gm.peliculas.domain.Pelicula;
import mx.com.gm.peliculas.excepciones.AccesoDatosEx;
import mx.com.gm.peliculas.excepciones.EscrituraDatosEx;
import mx.com.gm.peliculas.excepciones.LecturaDatosEx;

public interface IAccesoDatos {

    public boolean existe() throws AccesoDatosEx;

    List<Pelicula> listar() throws LecturaDatosEx;

    void escribir(Pelicula pelicula, boolean anexar) throws EscrituraDatosEx;

    String buscar(String buscar) throws LecturaDatosEx;

    void crear(String nombreRecurso) throws AccesoDatosEx;

    void borrar() throws AccesoDatosEx;
}
