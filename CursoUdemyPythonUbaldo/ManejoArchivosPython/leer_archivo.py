try:
    # En el caso de que queramos abrir un archivo que se encuentra en otra carpeta se debera de especificar la ruta de windows, mac o linux
    archivo = open('prueba.txt', 'r', encoding = 'utf8')
    # print(archivo.read()) # Despues de que leamos el archivo ya se habra
    # terminado de leer el archivo, asi que no podremos volver a leerlo
    # Leer algunos caracteres
    # archivo.read(cantidad de caracteres que queremos leer)
    # estos se acumularan asi que queremos volver a ejecutarlo
    # ya habriamos leido la cantidad que indicamos y leera
    # despues la otra cantidad si es que hay mas
    # print(archivo.read(5))
    # print(archivo.read(3))

    # Leer lineas completas
    print(archivo.readline())
    print(archivo.readline())
except BaseException as e:
    print(e)
