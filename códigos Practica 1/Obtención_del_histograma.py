import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en color
img0 = cv2.imread('OP1_4.jpg')
img=cv2.resize(img0,(500,500))

# Verificar si la imagen fue cargada correctamente
if img is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta.")

# Conversión de imagen a escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises usando matplotlib
cv2.imshow('Imagen en Grises', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Histograma de la imagen en escala de grises
plt.hist(gray_img.ravel(), 256, [0, 256])
plt.title('Histograma en Escala de Grises')
plt.xlabel('Intensidad de píxeles')
plt.ylabel('Frecuencia')
plt.show()

# Histograma de los canales de color
color = ('b', 'g', 'r')


for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
    
plt.title('Histograma de la Imagen en Color')
plt.xlabel('Intensidad de píxeles')
plt.ylabel('Frecuencia')
plt.show()
