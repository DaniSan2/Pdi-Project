import cv2

# Cargar la imagen en color
img0 = cv2.imread('OP1_4.jpg')
img=cv2.resize(img0,(500,500))

# Verificar si la imagen fue cargada correctamente
if img is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")

# 4. Conversión de imagen a escala de grises
# Convertir la imagen a escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostrar resultados
cv2.imshow('Imagen en Grises', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()