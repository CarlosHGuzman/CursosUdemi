package domain.manejojavabeanP2;

import java.io.Serializable;

public class Persona implements Serializable{
    private String nombre;
    private String apellido;
    
    //una clase de javabean se utiliza para que otras tecnologias como ivernate puedan utilizar esta clase
    //ademas para que sea bean se debe de implementar Serializable que se encuentra en java.io.Serializable
    //lo que permite esta interface serializable es enviar nuestra clase entre diferentes equipos
    public Persona(){//es obligatorio tener un constructor vacio
    }
    
    public Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
    
}
