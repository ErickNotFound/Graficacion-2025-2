import cv2 as cv
import numpy as np

img = np.ones((500,500,3), np.uint8)*150

# Dibuja un circulo grande amarillo (cara)
cv.circle(img, (255,255), 100, (0, 255, 255), -3)

# Dibuja dos circulos pequeños de color blanco (ojos)
cv.circle(img, (220,220), 30, (255, 255, 255), -2)
cv.circle(img, (220,220), 10, (51, 0, 0), -1)

# Dibuja dos circulos pequeños de color negro (ojos)
cv.circle(img, (290,220), 30, (255, 255, 255), -1)
cv.circle(img, (290,220), 10, (51, 0, 0), -1)

# Dibuja una boca (rectángulo)
cv.rectangle(img, (240,260), (315,300), (51,0,0), -1)

# Muestra la imagen
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()