import cv2 # con esto importamos a cv 
# nombreVariable cv2.imread('nombre o direccion completa de la imagen') esto es para cargarla en la variabble
imagen = cv2.imread('C:\\Users\\USUARIO\\Documents\\CursosUdemi\\DocPythoNoMathRecocomientoFacial\\contorno.jpg')
#cv2.imshow('Titulo de la ventana', nombreVariable)
cv2.imshow('Imagen', imagen) 
# cv2.waitKey(parametro de 0 o 1) es para impedir que se cierre automaticamente
cv2.waitKey(0) # valor de 1 todo es fluido(cuando utilizamos video o camara) valor de 0 estatico
# cv2.destroyAllWindows() lo que va hacer es que cerrara todas las pestañas abiertas
cv2.destroyAllWindows()