package palabrathis;

public class PalabraThis {
    public static void main(String[] args) {
        Persona persona = new Persona("Juan", "Perez");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre:" + persona.nombre);
        System.out.println("persona nombre:" + persona.apellido);
    }
}

class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
