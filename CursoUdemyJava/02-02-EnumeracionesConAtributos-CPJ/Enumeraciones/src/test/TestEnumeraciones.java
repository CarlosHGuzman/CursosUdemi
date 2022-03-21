package test;

import enumeracion.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        System.out.println("Dia 1:" + Dias.LUNES );
        indicarDiaSemana(Dias.MARTES);
    }
    
    private static void indicarDiaSemana(Dias dias){
        switch(dias){
            case LUNES:
                System.out.println("Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Segundo dia de la semana");
        }
    }
}
