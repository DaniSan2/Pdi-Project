#imagen =cv2.resize(image,(500,500))

import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('OP1_4.jpg')
newimg= cv2.resize(img,(500,500))
# Operaciones aritméticas
suma = cv2.add(img, 50) # Suma un escalar
resta = cv2.subtract(img, 50) # Resta un escalar
multiplicacion = cv2.multiply(img, 1.2) # Multiplica por un escalar

# Mostrar resultados
imgsuma= cv2.resize(suma,(500,500))
imgres= cv2.resize(resta,(500,500))
imgmul= cv2.resize(multiplicacion,(500,500))
cv2.imshow('Imagen Original', newimg)
cv2.imshow('Imagen Suma', imgsuma)
cv2.imshow('Imagen Resta', imgres)
cv2.imshow('Imagen Multiplicación', imgmul)
cv2.waitKey(0)

cv2.destroyAllWindows()