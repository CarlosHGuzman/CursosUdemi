package ManejoGenericsP4.ApiColeccionGenericas;

import ManejoGenericsP3.ApiColeccionGenericas.*;
import java.util.*;
import javax.swing.JOptionPane;

public class TestColeccionesGenericas {

    public static void main(String[] args) {
        //Podemos indicar que la lista va ser de un tipo en especifico con la notacion de diamante
        List<String> miLista = new ArrayList<>();
        //Ya que no estamos utilizando un tipo tan generico como lo es object
        //Solo podremos agregar valores de tipo String;
        miLista.add("Lunes");
        miLista.add("Martes");
        miLista.add("Miercoles");
        miLista.add("Jueves");
        miLista.add("Viernes");
        miLista.add("Sabado");
        miLista.add("Domingo");
        String elemento = miLista.get(0); //Trabajar con el tipo definido nos evita hacer conversiones en caso de que se requiera
        //imprimir(miLista);

        Set<String> miSet = new HashSet<>(); //Este no garantiza que se mantenga el orden en que se agregaron
        miSet.add("Lunes");
        miSet.add("Martes");
        miSet.add("Miercoles");
        miSet.add("Jueves");
        miSet.add("Viernes");
        miSet.add("Sabado");
        miSet.add("Domingo");
        miSet.add("Domingo"); //No se puede repetir los elementos que ya existen.
//        imprimir(miSet);
        
        //Podemos elegir el tipo tanto para la llave como para el valor
        Map<String, String> miMapa = new HashMap<>();
        miMapa.put("Llave 1", "valor 1");// para cargar valores se debe utilizar mapa.put(llave, valor); llave:valor;
        miMapa.put("Llave 2", "valor 2");
        miMapa.put("Llave 3", "valor 3");
        miMapa.put("Llave 3", "Carlos"); //No se puede repetir el valor de la llavae ya que esto hara que se reemplaze su valor
        //por el ultimo que ingresamos
        
        String elementoMapa = miMapa.get("Llave 1"); // se utilza para obtener el valor
        System.out.println("elemento mapa = " + elementoMapa);
        
        //para obtener las llaves se utiliza el metodo mapa.keySet(); el cual regresa
        //un set de las llaves por ende no se imprimira en orden
        imprimir(miMapa.keySet());
        
        //para obtener todos los valores de las llaves se utiliza el metodo mapa.values(); el cual regresa
//        un set de los valores por ende no se imprimira en orden
        imprimir(miMapa.values());
    }

    //Se puede seguir utilizando el tipo generico ya que no hay problema, pero tambien podemos
    //declarar que la coleccion que se va recibir va ser de un tipo en especifico
    //Una ventaja que tiene trabajar con tipos mas especificos es que podremos utilizar sus metodos
    public static void imprimir(Collection<String> coleccion) {
        Object seguir = JOptionPane.showInputDialog(null, "Como dese recorrer la coleccion: ", "Impresion coleccion", JOptionPane.QUESTION_MESSAGE, null, new Object[]{"for each", "Lambda"}, "for each");
        if ("for each".equals((String) seguir)) {
            for (Object elemento : coleccion) {
                System.out.println(coleccion.getClass() + " Elemento = " + elemento);
            }
        } else if ("Lambda".equals((String) seguir)) {
            //ArrayList.forEach(variable que va a recorrer ->{ bloque codigo});
            coleccion.forEach(elemento -> {
                System.out.println(coleccion.getClass() + " Elemento = " + elemento);
            });
        } else {
            System.out.println("No se reconoce la opción");
        }
    }
}