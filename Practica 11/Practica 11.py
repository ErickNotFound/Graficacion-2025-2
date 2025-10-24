# Practica 11: Calculo de filtro lineal. Escarlar la imagen y rellenar usando el filtro compañeros mas cercano (modo raw)

import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread(r"C:\imagenes\image.png", 0)
if img is None:
    raise ValueError("La imagen no se pudo cargar. Verifica la ruta del archivo.")
# Obtener el tamaño de la imagen
x, y = img.shape
# Definir el factor de escala
scale_x, scale_y = 2, 2

# Crear nueva imagen vacía
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)

# escalar la imagen (asignar píxeles)
for i in range(x):
    for j in range(y):
        scaled_img[i * scale_y, j * scale_x] = img[i, j]

# Rellenar usando el algoritmo de vecino más cercano
for i in range(scaled_img.shape[0]):
    for j in range(scaled_img.shape[1]):
        if scaled_img[i, j] == 0:  # píxel vacío
            # Calcular el píxel original más cercano
            orig_x = int(i / scale_y)
            orig_y = int(j / scale_x)
            scaled_img[i, j] = img[orig_x, orig_y]

# Mostrar imágenes
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (Nearest Neighbor)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()