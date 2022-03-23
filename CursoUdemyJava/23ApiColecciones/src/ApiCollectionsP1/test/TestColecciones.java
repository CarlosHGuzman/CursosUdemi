package ApiCollectionsP1.test;

import java.util.*;

public class TestColecciones {
    public static void main(String[] args){
        List miLista = new ArrayList();
        miLista.add("Lunes");
        miLista.add("Martes");
        miLista.add("Miercoles");
        miLista.add("Jueves");
        miLista.add("Viernes");
        miLista.add("Sabado");
        miLista.add("Domingo");
        
        for(Object elemento: miLista){
            System.out.println("Elemento (for each) = " + elemento);
        }
        
        //ArrayList.forEach(variable que va a recorrer ->{ bloque codigo});
        miLista.forEach(elemento -> {
            System.out.println("Elemento = (Lambda)" + elemento);
        });
    }
}
