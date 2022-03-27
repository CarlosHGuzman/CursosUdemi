package ManejoGenericsP1.genericos;

import javax.swing.JOptionPane;

public class ClaseGenerica<T> {
/*
<E> Podemos agregar un elemento de cierto tipo, pero el tipo lo vamos a especificar hasta que utilicemos la clase.
<K> Se utilza para definir una llave(LLave, utilizado en mapas)
<N> Number (Utilizado para números)
<T> Type (representa un tipo, es decir, una clase)
<V> Value(representa un valor, tambien se utiliza en mapas)
S, U, V etc. usado para representas otros tipos.
*/
    private T objeto; //Se debe de crear un atributo de tipo T para inicializar el tipo
    public ClaseGenerica(T objeto){
        this.objeto = objeto; 
    }
    public void obtenerTipo(){
        JOptionPane.showMessageDialog(null, "El tipo T es: " + objeto.getClass().getSimpleName());
    }
}
