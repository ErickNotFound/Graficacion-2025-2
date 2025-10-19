import cv2 as cv
import numpy as np
import math

img = cv.imread(r"C:\imagenes\image.png", 0)
if img is None:
    raise ValueError("La imagen no se pudo cargar. Verifica la ruta del archivo.")

x, y = img.shape

rotated_img = np.zeros((x*2, y*2), dtype=np.uint8)

xx, yy = rotated_img.shape

cx, cy = int(x // 2), int(y // 2)

angle = 45
tetha = math.radians(angle)

for i in range(x):
    for j in range(y):
        new_x = int(i * math.cos(tetha) - j * math.sin(tetha))
        new_y = int(-i * math.sin(tetha) + j * math.cos(tetha))
        if 0 <= new_x < y and 0 <= new_y < x:
            rotated_img[new_y, new_x] = img[i, j]

cv.imshow('Rotated', rotated_img)
cv.imshow('Original', img)
cv.waitKey(0)
cv.destroyAllWindows()
