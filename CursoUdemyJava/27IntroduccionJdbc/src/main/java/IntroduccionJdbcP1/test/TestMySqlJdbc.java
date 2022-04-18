package IntroduccionJdbcP1.test;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JOptionPane;

public class TestMySqlJdbc {
    public static void main(String[] args){
        //cadena de conexion hacia la base de datos
        String url = "jdbc:mysql://127.0.0.1:3306/test?useSSL=false&useTimezone=true&serverTimezone=UTC&allowPublicKeyRetrieval=true";
        //jdbc:mysql:id:puerto/basededatos?useSSL=conexionsegura&useTImeZone=zonahoraria&serverTimeZone=Zonahoraria&allowPublicKeyRetrieval=conectarDeFormaExitosaAMysql
        try{
            // Esta linea se suele utilizar para conectarse de forma exitosa a nuestra base de datos en el caso de que trabajemos con una aplicacion web
            // Class.forName("com.mysql.cj.jdbc.Driver"); 
            Connection conexion = DriverManager.getConnection(url, "root", "3407");
            Statement instruccion = conexion.createStatement(); //permite ejecutar instrucciones de mysql
            var sql = "Select idpersona, nombre, apellido, email, telefono from test.persona";
            ResultSet resultado = instruccion.executeQuery(sql);
            String unir = "";
            while(resultado.next()){//el metodo .next va a iterar mientras haya algo que iterar
                unir += "\nId persona: " + resultado.getInt("idpersona") + " Nombre: " + resultado.getString("nombre")
                        + " Apellido: " + resultado.getString("apellido") + " Email: " + resultado.getString("email")
                        + " Telefono: " + resultado.getString("telefono");
            }
            JOptionPane.showMessageDialog(null, "Resultado de la busqueda: " + unir, "Resultado", 1);
            resultado.close(); instruccion.close(); conexion.close(); //Cerramos los recursos
        }catch(SQLException ex){
            ex.printStackTrace(System.out);
            System.out.println("Error al conectarse con la base de datos");
        } /*catch (ClassNotFoundException ex) {
            ex.printStackTrace(System.out);
        }*/
    }
}
