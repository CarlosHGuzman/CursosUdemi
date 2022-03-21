package domain.manejojavabeanP2.test;

import domain.manejojavabeanP2.Persona;
import javax.swing.JOptionPane;

public class TestJavaBeans {
    public static void main(String[] args){
        Persona persona = new Persona(); //Se debe de crear el objeto con el constructor vacio  
        //ascerilacion conversion del objeto a binario
        //desacerilacion conversion de binario a objeto todo esto lo hace la interface serializable
        persona.setNombre("manuel");
        persona.setApellido("Hurtado");
        
        JOptionPane.showMessageDialog(null, persona);
        JOptionPane.showMessageDialog(null, "Persona nombre: " + persona.getNombre());
        JOptionPane.showMessageDialog(null, "Persona apellido: " + persona.getApellido());
    }
}
