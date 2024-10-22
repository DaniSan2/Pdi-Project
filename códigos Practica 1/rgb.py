import cv2
import numpy as np

# Cargar la imagen desde el archivo
imagen = cv2.imread('OP1_4.jpg')

# Comprobar si la imagen fue cargada correctamente
if imagen is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta y el archivo.")
else:
    # Redimensionar la imagen a un tamaño específico (por ejemplo, 500x500 píxeles)
    nueva_imagen = cv2.resize(imagen, (500, 500))

    # Mostrar la imagen original
    cv2.imshow('Imagen Original', nueva_imagen)


    # Extraer los canales de color
    b, g, r = cv2.split(nueva_imagen)

    # Crear imágenes en las que solo se muestre el canal correspondiente en su color
    cero = np.zeros_like(b)  # Matriz de ceros del mismo tamaño que los canales

    # Mostrar el canal rojo con el color rojo
    rojo = cv2.merge([cero, cero, r])
    cv2.imshow('Canal Rojo', rojo)

    # Mostrar el canal verde con el color verde
    verde = cv2.merge([cero, g, cero])
    cv2.imshow('Canal Verde', verde)

    # Mostrar el canal azul con el color azul
    azul = cv2.merge([b, cero, cero])
    cv2.imshow('Canal Azul', azul)

    # Esperar a que se presione una tecla para cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
