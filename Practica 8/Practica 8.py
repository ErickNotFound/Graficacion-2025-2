# Practica 8: Detección de rostros y dibujo de figuras geométricas
# Agregar una nariz, boca y orejas a la cara detectada.
# Y colocar las figuras de manera proporcional a la cara.
# Por ejemplo, si la cara es grande, las figuras deben ser grandes. Mantener la proporción.

import cv2 as cv 

rostro = cv.CascadeClassifier(r"C:\archivos\haarcascade_frontalface_alt.xml")
cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gris, 1.3, 5)
    for(x,y,w,h) in rostros:
        res = int((w+h)/8)
        img = cv.rectangle(img, (x,y), (x+w, y+h), (234, 23,23), 5)
        img = cv.rectangle(img, (x,int(y+h/2)), (x+w, y+h), (0,255,0),5 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 21, (0, 0, 0), 2 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 20, (255, 255, 255), -1 )
        img = cv.circle(img, (x + int(w*0.3), y + int(h*0.4)) , 5, (0, 0, 255), -1 )
        img = cv.circle(img, (x + int(w*0.7), y + int(h*0.4)) , 5, (0, 0, 255), -1 )

    cv.imshow('img', img)
    if cv.waitKey(15) & 0xFF == 27:  
        break
    
cap.release
cv.destroyAllWindows()