from cv2 import CHAIN_APPROX_SIMPLE, RETR_LIST, GaussianBlur, cv2, drawContours
import numpy as np

original = cv2.imread('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\DocPythoNoMathRecocomientoFacial\\monedassoles.jpg')
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
# desenfoque = cv.GuassianBlur(imagen procesar, (parametros si queremos que se haga bonito o desenfocado), 0)
valorGauss = 1
valorKernel = 35
gauss = cv2.GaussianBlur(grises, (valorGauss, valorKernel), 0)

# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html
# bordes = cv2.Canny(gauss, )
canny = cv2.Canny(gauss, 60, 100)

# https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html
kernel = np.ones((valorKernel, valorKernel), np.uint8)    # esto lo pasamos a enteros debido a que nos puede arrojar valores de tipo doble                     
erosion = cv2.erode (canny, kernel, 5) # esto lo que hace es reducir nuestra imagen para reducir el ruido
dilatación = cv2.dilate (canny, kernel,  5) # esto lo que hace es aumentar el tamaño de la imagen para reducir el ruido
cierre = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contornos, jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontrada: {}".format(len(contornos)))
cv2.drawContours(original, contornos, -1, (0,0,255), 2)
# Mostrar resultado
# cv2.imshow('Erosionado', erosion)
# cv2.imshow('Dilatado', dilatación)
# cv2.imshow("Grises", grises)
# cv2.imshow("Gauss", gauss)
# cv2.imshow("canny", canny)
cv2.imshow('Resultado',original)
# cv2.imshow('Cierre', cierre)
cv2.waitKey(0)