# CLASE 100 (FELICITACIONES) CONEXION DE PYTHON A POSTGRESQL
# import psycopg2 # con este paquete ya podemos conectarnos a postgreSQL
#
# # Objeto de tipo conexion
# conexion = psycopg2.connect(
#     user='postgres', # El usuario que en este caso es el que viene  por default
#     password='admins', # La contraseña
#     host='127.0.0.1', # La direccion ip
#     port=5432, # El numero del puerto
#     database='test_db' # Nombre de la base de datos
#     )
# # print(conexion) # Nos permite mirar si establecimos conexion
#
# # Un cursor nos vamos a permitir ejecutar sentencia postgreSQL en python
# cursor = conexion.cursor() # nombreVariable = objetoConexion.cursor()
# sentencia = 'SELECT * FROM persona' # El query que queremos ejecutar
# cursor.execute(sentencia) # objetoCursor.execute(sentencia) para ejecutar nuestra sentencia
# registros = cursor.fetchall() # Va almacenar todos lo valores de la sentencia que ejecutamos
# print(registros)
# for line in registros:
#     print(registros)
#
# cursor.close() # Esto es para cerrar el objeto cursor que nos permite ejecutar sentencias
# conexion.close() # Esto es para cerrar la conexion


# CLASE 101 USO DE WITH Y PSYCOPG
import psycopg2  # con este paquete ya podemos conectarnos a postgreSQL

# Objeto de tipo conexion
conexion = psycopg2.connect(
    user='postgres',  # El usuario que en este caso es el que viene  por default
    password='admins',  # La contraseña
    host='127.0.0.1',  # La direccion ip
    port=5432,  # El numero del puerto
    database='test_db'  # Nombre de la base de datos
)
# print(conexion) # Nos permite mirar si establecimos conexion

# Un cursor nos vamos a permitir ejecutar sentencia postgreSQL en python
try:
    with conexion: # el with no cerrara la conexion en automatico por ende colocamos finally conexion.close()
        with conexion.cursor() as cursor:  # nombreVariable = objetoConexion.cursor() a diferencia de la conexion
            # el with para el cursor si lo cerrar en automatico
            sentencia = 'SELECT * FROM persona'  # El query que queremos ejecutar
            cursor.execute(sentencia)  # objetoCursor.execute(sentencia) para ejecutar nuestra sentencia
            registros = cursor.fetchall()  # Va almacenar todos lo valores de la sentencia que ejecutamos
            print(registros)
            for line in registros:
                for i in range(0, len(line)):
                    print(f'{line[i]}', end='\t ')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()  # Esto es para cerrar la conexion
