anotaciones = open('Anotaciones.docx', 'w+', encoding = 'utf8')
anotaciones.write('''
Por colores no se pueden hacer operaciones, todas las imagenes tienen colores basicos
RGB: Red, Green, Blue
Operaciones: 
- Escala de grises: Se pasa todas las imagenes de colores a escala de grises
- Umbralización: Esto es para diferenciar entre el objeto que se quiere analizar
y el espacio donde se encuentra
Representacion de contornos:
Segmentacion: Es reconocer la imagen como si fuera una figura geometrica
Contorno: Limites del objeto    
''')
for line in anotaciones:
    print(line)
anotaciones.close()