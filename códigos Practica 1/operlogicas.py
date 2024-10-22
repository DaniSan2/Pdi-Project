import cv2
import numpy as np

# Cargar dos imágenes
img1 = cv2.imread('OP1_4.jpg')
img2 = cv2.imread('OP1_1.jpg')

# Asegurarse de que las imágenes tengan el mismo tamaño
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Operaciones lógicas
and_img = cv2.bitwise_and(img1, img2)
or_img = cv2.bitwise_or(img1, img2)
xor_img = cv2.bitwise_xor(img1, img2)

# Mostrar resultados
img3 = cv2.resize(and_img, (500, 500))
img4 = cv2.resize(or_img, (500, 500))
img5 = cv2.resize(xor_img, (500, 500))
cv2.imshow('Imagen AND', img3)
cv2.imshow('Imagen OR', img4)
cv2.imshow('Imagen XOR', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()