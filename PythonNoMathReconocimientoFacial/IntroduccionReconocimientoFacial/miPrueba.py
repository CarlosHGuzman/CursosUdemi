import cv2
imagen = cv2.imread("C:\\Users\\USUARIO\\Pictures\\Camera Roll\\WIN_20211002_20_41_37_Pro.jpg")
grises = cv2.cvtColor(imagen,  cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY)
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contorno, -1,(65, 105, 225), 3)

cv2.imshow('Imagen mia', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()