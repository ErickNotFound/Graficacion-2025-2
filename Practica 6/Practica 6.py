# Practica 6: Trasnformaciones Geométricas con dos imágenes
# Realizar las siguientes transformaciones geométricas:
# - Trasladar la primera imagen al centro de la segunda imagen.
# - Rotar la primera imagen 20 grados.
# - Escalar la primera imagen al 0.8 de su tamaño original.
# - Rotar la imagen escalada 40 grados.
# - Escalar la imagen rotada al 2.0 de su tamaño original.
# a la segunda imagen realizar las siguientes transformaciones:
# - Rotar la imagen 60 grados.
# - Escalar la imagen al 0.5 de su tamaño original.

import cv2 as cv
import numpy as np

img = cv.imread(r"C:\imagenes\image.png", 0)
img2 = cv.imread(r"C:\imagenes\hlx.jpg", 0)

if img is None or img2 is None:
    raise ValueError("No se pudieron cargar las imágenes.")

x, y = img.shape
x2, y2 = img2.shape

# 1. Trasladar la primera imagen al centro de la segunda imagen.

dx, dy = x2  // 2, y2 // 2

M = np.float32([[1, 0, dx], [0, 1, dy]])

img_transofrmada = cv.warpAffine(img, M, (y, x))

# 2. Rotar la primera imagen 20 grados.

centro_img = (y // 2, x // 2)

angulo = 20

M = cv.getRotationMatrix2D(centro_img, angulo, 1.0)

img_transofrmada = cv.warpAffine(img_transofrmada, M, (y, x))

# 3. Escalar la primera imagen al 0.8 de su tamaño original.

escalado_X, escalado_Y = 0.8, 0.8

img_transofrmada = cv.resize(img_transofrmada, None, fx=escalado_X, fy=escalado_Y, interpolation=cv.INTER_CUBIC)

# 4. Rotar la imagen escalada 40 grados.

angulo = 40

M = cv.getRotationMatrix2D(centro_img, angulo, 1.0)

img_transofrmada = cv.warpAffine(img_transofrmada, M, (y, x))

# 5. Escalar la imagen rotada al 2.0 de su tamaño original.

escalado_X, escalado_Y = 2.0, 2.0

img_transofrmada = cv.resize(img_transofrmada, None, fx=escalado_X, fy=escalado_Y, interpolation=cv.INTER_CUBIC)

# De la segunda imagen:
# 1. Rotar la imagen 60 grados.

centro_img2 = (y2 // 2, x2 // 2)
angulo2 = 60
M = cv.getRotationMatrix2D(centro_img2, angulo2, 1.0)
img2_transformada = cv.warpAffine(img2, M, (y2, x2))

# 2. Escalar la imagen al 0.5 de su tamaño original.

escalado_X2, escalado_Y2 = 0.5, 0.5
img2_transformada = cv.resize(img2_transformada, None, fx=escalado_X2, fy=escalado_Y2, interpolation=cv.INTER_CUBIC)

cv.imshow('Imagen Original', img)
cv.imshow('Imagen Original 2', img2)
cv.imshow('Imagen Transformada', img_transofrmada)
cv.imshow('Imagen Transformada 2', img2_transformada)

cv.waitKey(0)
cv.destroyAllWindows()