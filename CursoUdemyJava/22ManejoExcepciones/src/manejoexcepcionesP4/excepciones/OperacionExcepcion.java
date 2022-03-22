package manejoexcepcionesP4.excepciones;

public class OperacionExcepcion extends Exception{
    //tiene que extender de una de las clases del api de java (exception-RuntimeException-NullPointerException-SQLException
    //Si se hereda de exception el compilador nos va a obligar a procesar la excepcion porque es de tipo checkexception
    //Si se hereda de la clase RuntimeException no nos obliga a procesar la excepcion
    
    public OperacionExcepcion(String mensaje){
        super(mensaje);
    }
}
