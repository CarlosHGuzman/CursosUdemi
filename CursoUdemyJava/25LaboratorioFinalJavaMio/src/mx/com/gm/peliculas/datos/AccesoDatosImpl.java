package mx.com.gm.peliculas.datos;

import java.io.*;
import java.util.*;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import mx.com.gm.peliculas.domain.Pelicula;
import mx.com.gm.peliculas.excepciones.*;

public class AccesoDatosImpl implements IAccesoDatos{
    private String nombreRecurso = "archivo.txt";
    
    @Override
    public boolean existe() throws AccesoDatosEx {// no es necesario que se declare el accesoDatoex ya que no arroja error
        if(nombreRecurso == null){
            return false;
        }else{
            File archivo = new File(nombreRecurso);
            return archivo.exists(); //Con el metodo exist(); podemos mirar si existe o no el archivo
        }
    }

    @Override
    public List<Pelicula> listar() throws LecturaDatosEx {
        File archivo = new File(nombreRecurso);
        List<Pelicula> peliculas = new ArrayList<>();
        try {
            BufferedReader entrada = new BufferedReader(new FileReader(archivo));
            String linea = null;
            linea = entrada.readLine();
            while(linea != null){
                Pelicula pelicula = new Pelicula(linea);
                peliculas.add(pelicula);
                linea = entrada.readLine();
            }
            entrada.close();
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
            throw new LecturaDatosEx("Excepcion al listar peliculas: " + ex.getMessage());
        } catch (IOException ex) {
            ex.printStackTrace(System.out);
            throw new LecturaDatosEx("Excepcion al listar peliculas: " + ex.getMessage());
        }
        return peliculas;
    }

    @Override
    public void escribir(Pelicula pelicula, boolean anexar) throws EscrituraDatosEx {
        File archivo = new File(nombreRecurso);
        try {
            PrintWriter salida = new PrintWriter(new FileWriter(archivo, anexar));
            salida.println(pelicula.toString());
            salida.close();
            System.out.println("Se ha escrito informacion al archivo: " + pelicula);
        } catch (IOException ex) {
            ex.printStackTrace(System.out);
            throw new EscrituraDatosEx("Excepcion al escribir peliculas: " + ex.getMessage());
        }
    }

    @Override
    public String buscar(String buscar) throws LecturaDatosEx {
        File archivo = new File(nombreRecurso);
        String resultado = null;
        try {
            BufferedReader entrada = new BufferedReader(new FileReader(archivo));
            String linea = null;
            linea = entrada.readLine();
            int indice = 1;
            while(linea != null){
                if(buscar != null && buscar.equalsIgnoreCase(linea)){
                    resultado = "Pelicula " + linea + " encontrada en el indice " + indice;
                    break;
                }
                linea = entrada.readLine();
                indice++;
            }
            entrada.close();
        } catch (FileNotFoundException ex) {
            ex.printStackTrace(System.out);
            throw new LecturaDatosEx("Excepcion al buscar pelicula");
        } catch (IOException ex) {
                        ex.printStackTrace(System.out);
            throw new LecturaDatosEx("Excepcion al buscar pelicula");
        }
        return resultado;
    }

    @Override
    public void crear(String nombreRecurso) throws AccesoDatosEx {
        this.nombreRecurso = nombreRecurso;
        var archivo = new File(nombreRecurso);
        try {
            var salida = new PrintWriter(new FileWriter(archivo));
            salida.close();
            System.out.println("Se ha creado el archivo");
        } catch (IOException ex) {
            ex.printStackTrace();
            throw new AccesoDatosEx("Excepcion al crear archivo:" + ex.getMessage());

        }
    }

    @Override
    public void borrar() throws AccesoDatosEx { // no es necesario que se declare el accesoDatoex ya que no arroja error
        File archivo = new File(nombreRecurso);
        if(archivo.exists()){
            archivo.delete();
        }
        System.out.println("Se ha borrado el archivo");
    }
    
    public String getNombreRecuros(){
        return this.nombreRecurso;
    }
}
