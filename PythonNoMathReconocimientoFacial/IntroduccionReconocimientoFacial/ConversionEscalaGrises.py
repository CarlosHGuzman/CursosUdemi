# cv2. findCountours(umbral, mode, method) lo que va hacer es encontrar todos
# los contornos 
'''
Umbral = imagen en blanco y negro 
mode = como quieres que se de el resultado puede ser lista, array, promediar
method = hay dos funciones de encontrar los contornos 
    - APROX_NONE = Va a encontrar todo apartir de marcar el objeto con puntos 
    - APROX_SIMPLE = Va a encontrar los limites y promedia lo de APROX_NONE
'''
from cv2 import cv2
imagen = cv2.imread('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\DocPythoNoMathRecocomientoFacial\\contorno.jpg')
# https://docs.opencv.org/4.5.3/d8/d01/group__imgproc__color__conversions.html
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# https://docs.opencv.org/3.4.15/da/d97/tutorial_threshold_inRange.html
# El metodo devuelve dos salidas. El primero es el umbral que se utilizo y el segundo
# resultado es la imagen de umbral 
_, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY) # _ ignora el resultado, es decir no existe variable pero nos permite ejecutar el programa
# print(tipoUmbral)


# https://docs.opencv.org/3.4.15/df/d0d/tutorial_find_contours.html
# (imagen de origen, metodo de recuperacion, aproximacion de contorno)
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
# (imagen origen, contours, orden, (color del contorno rgb), grosor de entorno)
cv2.drawContours(imagen, contorno, -1,(65, 105, 225), 3)

# Mostrar
cv2.imshow('Imagen en grises', grises)
cv2.imshow('Imagen original ', imagen)
cv2.imshow('Imagen con umbral', umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()