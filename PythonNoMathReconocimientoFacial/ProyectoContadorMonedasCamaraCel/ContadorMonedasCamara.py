import cv2 as cv
import numpy as np
# El valor de 0 es para capturar las camaras que este trabajando en el computador
capturaVideo = cv.VideoCapture(0) 
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    _,Camara = capturaVideo.read()
    grises = cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)    # esto lo pasamos a enteros debido a que nos puede arrojar valores de tipo doble                     
    gauss = cv.GaussianBlur(grises, (3, 5), 0)
    canny = cv.Canny(gauss, 60, 100)
    dilatación = cv.dilate (canny, kernel,  5)
    cierre = cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)
    cv.imshow('En vivo', canny)
    if cv.waitKey(1) == ord('q'): 
        break
capturaVideo.release() # Detemos el video
cv.destroyAllWindows()