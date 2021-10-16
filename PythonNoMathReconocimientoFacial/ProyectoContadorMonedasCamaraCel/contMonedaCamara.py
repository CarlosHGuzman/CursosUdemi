from cv2 import CHAIN_APPROX_SIMPLE, COLOR_BGR2GRAY, RETR_EXTERNAL, RETR_LIST, THRESH_BINARY, THRESH_BINARY_INV, GaussianBlur, contourArea, cv2 as cv, drawContours, findContours, moments, threshold
import numpy as np
def ordenarPuntos(puntos):
    n_puntos = np.concatenate(puntos[0], puntos[1], puntos[2], puntos[3]).tolist()
    y_order = sorted(n_puntos, key = lambda n_puntos: n_puntos[1]) # Lo que va hacer es ordenar los puntos
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key = lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key = lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alineamiento(imagen, ancho, alto):
    imagen_alineada = None
    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    tipoUmbral, umbral = cv.threshold(grises, 0, 255, cv.THRESH_BINARY)
    cv.imshow('Umbral', umbral)
    contornos, jerarquia = cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contornos, key = cv.contourArea, reverse = True)[:1]
    for c in contorno:
        # https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
        epsilon =  0.01 * cv.arcLength(c, True) # Es para que las curvas no tengan tanto ruido
        approximacion = cv.approxPolyDP(c, epsilon, True)
        if len(approximacion) == 4:
            puntos = ordenarPuntos(approximacion)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0, 0], [ancho, 0], [0, alto], [ancho, alto]])
            M = cv.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada = cv.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada

capturaVideo = cv.videoCaptura(0)
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()

while True:
    tipoCamara, camara = cv.capturaVideo.read()
    if tipoCamara == False:
        break
    imagen_A6 =  alineamiento(camara, ancho = 480, alto = 677)
    if imagen_A6 is not None:
        puntos = []
        imagen_gris = cv.cvtColor(imagen_A6, cv.COLOR_BGR2GRAY)
        blur = GaussianBlur(imagen_gris, (5,6), 1) # Desenfoque
        _, umbral_2 = threshold(blur, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY_INV)
        cv.imshow("Umbral", umbral_2)
        contorno2, jerarquia = findContours(umbral_2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6, contorno2, -1, (255, 0, 0), 2)
        suma1 = 0.0
        suma2 = 0.0
        for c_2 in contorno2:
            area = cv.contourArea(c_2)
            Momentos = cv.moments(c_2)
            if(Momentos['m00'] == 0):
                Momentos['m00'] = 1.0
            x = int(Momentos['m10'] / Momentos['moo'])
            y = int(Momentos['m01']/ Momentos['m00'])
            
            if
