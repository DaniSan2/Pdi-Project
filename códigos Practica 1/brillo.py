import cv2
import numpy as np

# Función para aplicar corrección Gamma
def ajuste_gamma(imagen, gamma=1.0):
    if gamma < 0.01:  # Evitar la división por cero
        gamma = 0.01
    inv_gamma = 1.0 / gamma
    tabla = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype('uint8')
    return cv2.LUT(imagen, tabla)

# Función para ajustar brillo y contraste
def ajustar_brillo_contraste(imagen, brillo=0, contraste=0):
    beta = brillo - 100
    alpha = contraste / 100.0 + 1.0
    return cv2.convertScaleAbs(imagen, alpha=alpha, beta=beta)

# Función para actualizar la imagen con los parámetros actuales
def actualizar_imagen(val):
    brillo = cv2.getTrackbarPos('Brillo', 'Ajustes')
    contraste = cv2.getTrackbarPos('Contraste', 'Ajustes')
    gamma = cv2.getTrackbarPos('Gamma', 'Ajustes') / 100.0
    
    # Aplicar ajustes de brillo y contraste
    imagen_ajustada = ajustar_brillo_contraste(imagen_original, brillo, contraste)
    
    # Aplicar corrección Gamma
    imagen_gamma = ajuste_gamma(imagen_ajustada, gamma)
    
    # Mostrar la imagen resultante
    cv2.imshow('Ajustes', imagen_gamma)

# Cargar la imagen desde el archivo
imagen_original = cv2.imread('OP1_4.jpg')

# Comprobar si la imagen fue cargada correctamente
if imagen_original is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta y el archivo.")
    exit()

# Redimensionar la imagen a un tamaño específico
imagen_original = cv2.resize(imagen_original, (500, 500))

# Crear una ventana para mostrar la imagen
cv2.namedWindow('Ajustes')

# Crear trackbars para brillo, contraste y corrección Gamma
cv2.createTrackbar('Brillo', 'Ajustes', 100, 200, actualizar_imagen)  # Valor inicial 100, rango de 0 a 200
cv2.createTrackbar('Contraste', 'Ajustes', 100, 200, actualizar_imagen)  # Valor inicial 100, rango de 0 a 200
cv2.createTrackbar('Gamma', 'Ajustes', 100, 300, actualizar_imagen)  # Valor inicial 100, rango de 0 a 300 (1.0 = 100)

# Llamar a la función una vez para mostrar la imagen inicial
actualizar_imagen(0)

# Esperar a que se presione la tecla 'Esc' para salir
while True:
    if cv2.waitKey(1) == 27:  # La tecla 'Esc' cierra el programa
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()
