package ApiCollectionsP3.test;

import java.util.*;

public class TestColecciones {

    public static void main(String[] args) {
        List miLista = new ArrayList();
        miLista.add("Lunes");
        miLista.add("Martes");
        miLista.add("Miercoles");
        miLista.add("Jueves");
        miLista.add("Viernes");
        miLista.add("Sabado");
        miLista.add("Domingo");
        imprimir(miLista);

        Set miSet = new HashSet(); //Este no garantiza que se mantenga el orden en que se agregaron
        miSet.add("Lunes");
        miSet.add("Martes");
        miSet.add("Miercoles");
        miSet.add("Jueves");
        miSet.add("Viernes");
        miSet.add("Sabado");
        miSet.add("Domingo");
        miSet.add("Domingo"); //No se puede repetir los elementos que ya existen.
        imprimir(miSet);
        
        Map miMapa = new HashMap();
        miMapa.put("Llave 1", "valor 1");// para cargar valores se debe utilizar mapa.put(llave, valor); llave:valor;
        miMapa.put("Llave 2", "valor 2");
        miMapa.put("Llave 3", "valor 3");
        
        String elemento = (String) miMapa.get("valor 1"); //Esto regresa un objeto por ende se debe de convertir 
        System.out.println("elemento " + elemento);
        
        //para obtener las llaves se utiliza el metodo mapa.keySet(); el cual regresa
        //un set de las llaves por ende no se imprimira en orden
        imprimir(miMapa.keySet());
        
        //para obtener todos los valores de las llaves se utiliza el metodo mapa.values(); el cual regresa
        //un set de los valores por ende no se imprimira en orden
        imprimir(miMapa.values());
    }

    public static void imprimir(Collection coleccion) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Como desea recorrer la coleccion: \n1. for each \n2. Lambda \nOpcion: ");
        int seguir = scanner.nextInt();
        if (seguir == 1) {
            for (Object elemento : coleccion) {
                System.out.println(coleccion.getClass() + " Elemento = " + elemento);
            }
        } else if (seguir == 2) {
            //ArrayList.forEach(variable que va a recorrer ->{ bloque codigo});
            coleccion.forEach(elemento -> {
                System.out.println(coleccion.getClass() + " Elemento = " + elemento);
            });
        } else {
            System.out.println("No se reconoce la opción");
        }
    }
}
