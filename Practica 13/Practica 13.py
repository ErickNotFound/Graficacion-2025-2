# Practica 13. Crear un programa que por medio de la camara detecte las manos y dibuje una calculadora en pantalla funcional
# Tambien debe permitir operar con la calculadora usando las manos

import cv2 as cv
import mediapipe as mp
import numpy as np

cap = cv.VideoCapture(0)

mp.drawing = mp.solutions.drawing_utils
mp.hands = mp.solutions.hands
hands = mp.hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

ret, frame = cap.read()
prev_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

botones = [ '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+']

# agrega una variable para almacenar las coordenadas x,y de los botones
botones_coordenadas = {}

global expresion, resultado

def dibujar_calculadora(frame):

    boton_w, boton_h = 70, 70
    inicio_x, inicio_y = 0, 0

    for renglon_idx, renglon in enumerate(botones):
        for col_idx, boton in enumerate(renglon):
            x = inicio_x + boton_w
            y = inicio_y + boton_h

            # almacena las coordenadas de cada boton
            botones_coordenadas[boton] = (inicio_x, inicio_y, x, y)

            cv.rectangle(frame, (inicio_x, inicio_y), (x, y), (200, 200, 200), 1)
            cv.putText(frame, boton, (x - 45, y - 24), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            if boton == "/" or boton == "*" or boton == "-" or boton == "+":
                inicio_x = 0
                inicio_y += boton_h
                
            else:
                inicio_x += boton_w

def verificar_presion(x, y):
    """Verifica si las coordenadas del dedo caen dentro de un botón."""
    for boton, (x1, y1, x2, y2) in botones_coordenadas.items():
        if x1 < x < x2 and y1 < y < y2:
            return boton
    return None


punto_anterior = None  # Coordenadas anteriores del dedo

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv.flip(frame, 1)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    dibujar_calculadora(frame)

    results = hands.process(cv.cvtColor(frame, cv.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            # Dibujar círculo en el dedo índice
            cv.circle(frame, (x, y), 8, (0, 0, 255), -1)

            # Si tenemos punto previo, calculamos flujo óptico
            if punto_anterior is not None:
                p0 = np.array([[punto_anterior]], dtype=np.float32)
                p1, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, p0, None, **lk_params)

                if st[0][0] == 1:
                    x_nuevo, y_nuevo = p1[0][0]
                    cv.line(frame, (int(punto_anterior[0]), int(punto_anterior[1])),
                            (int(x_nuevo), int(y_nuevo)), (0, 255, 0), 2)

                    # Detectar si el movimiento fue rápido hacia abajo (simula un "toque")
                    mov_y = y_nuevo - punto_anterior[1]
                    if mov_y > 8:  # Puedes ajustar este umbral
                        boton_presionado = verificar_presion(int(x_nuevo), int(y_nuevo))
                        if boton_presionado:
                            print(f"Botón presionado: {boton_presionado}")
                            # añade el valor del botón a la expresión o calcula el resultado
                            if boton_presionado == "=":
                                try:
                                    resultado = eval(expresion)
                                    expresion = str(resultado)
                                except Exception as e:
                                    expresion = "Error"
                            else:
                                expresion += boton_presionado
                                
                            cv.putText(frame, f"{boton_presionado}", (300, 400),
                                       cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

                    punto_anterior = (x_nuevo, y_nuevo)

            else:
                punto_anterior = (x, y)

            prev_gray = gray_frame.copy()

    cv.imshow("Calculadora con manos y flujo óptico", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()