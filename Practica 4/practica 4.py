import cv2 as cv
import numpy as np
import random

width, height = 500, 500
x, y = 250, 250
radius = 30
dx, dy = 5, 3

# Posición inicial del círculo estático
static_x, static_y = 250, 250

while True:
    img = np.ones((height, width, 3), np.uint8) * 150
    cv.circle(img, (x, y), radius, (0, 255, 255), -1)
    cv.circle(img, (static_x, static_y), radius, (0, 255, 10), -1)
    cv.imshow('img', img)

    # Actualiza la posición
    x += dx
    y += dy

    # Rebote en los bordes
    if x - radius <= 0 or x + radius >= width:
        dx = -dx
    if y - radius <= 0 or y + radius >= height:
        dy = -dy

    # Detecta colisión entre círculos
    dist = ((x - static_x)**2 + (y - static_y)**2) ** 0.5
    if dist <= 2 * radius:
        # Cambia la posición del círculo estático aleatoriamente
        static_x = random.randint(radius, width - radius)
        static_y = random.randint(radius, height - radius)

    if cv.waitKey(15) & 0xFF == 27:  # Salir con ESC
        break

cv.destroyAllWindows()