# CLASE 100 (FELICITACIONES) CONEXION DE P YTHON A POSTGRESQL
import psycopg2 # con este paquete ya podemos conectarnos a postgreSQL

# Objeto de tipo conexion
conexion = psycopg2.connect(
    user='postgres', # El usuario que en este caso es el que viene  por default
    password='admins', # La contraseña
    host='127.0.0.1', # La direccion ip
    port=5432, # El numero del puerto
    database='test_db' # Nombre de la base de datos
    )
# print(conexion) # Nos permite mirar si establecimos conexion

# Un cursor nos vamos a permitir ejecutar sentencia postgreSQL en python
cursor = conexion.cursor() # nombreVariable = objetoConexion.cursor()
sentencia = 'SELECT * FROM persona' # El query que queremos ejecutar
cursor.execute(sentencia) # objetoCursor.execute(sentencia) para ejecutar nuestra sentencia
registros = cursor.fetchall() # Va almacenar todos lo valores de la sentencia que ejecutamos
print(registros)
for line in registros:
    print(registros)

cursor.close() # Esto es para cerrar el objeto cursor que nos permite ejecutar sentencias
conexion.close() # Esto es para cerrar la conexion