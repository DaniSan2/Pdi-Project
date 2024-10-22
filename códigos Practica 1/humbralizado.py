import cv2

img = cv2.imread('OP1_4.jpg')
img = cv2.resize(img, (500, 500))
# Convertir imagen a escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar umbralizado
_, threshold_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

# Mostrar resultados
cv2.imshow('Imagen Umbralizada', threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows()