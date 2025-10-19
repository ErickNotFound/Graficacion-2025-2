# Practica 7: Utilizando ecuaciones paramétricas, dibujar 10 figuras geométricas.

import numpy as np
import cv2

def create_ecuation_parametrica_draw(a, b, k, theta_increment, d):
    width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
    img = np.ones((height, width, 3), dtype=np.uint8)*255

    # Parámetros de la curva de Limacon
    max_theta = d * np.pi  # Un ciclo completo

    # Centro de la imagen
    center_x, center_y = width // 2, height // 2

    theta = 0  # Ángulo inicial

    while True:  # Bucle infinito
        # Limpiar la imagen
        #img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Dibujar la curva completa desde 0 hasta theta
        for t in np.arange(0, theta, theta_increment):
            # Calcular las coordenadas paramétricas (x, y) para la curva de Limacon
            r = a + b * np.cos(k * t)
            x = int(center_x + r * np.cos(t))
            y = int(center_y + r * np.sin(t))
            
            # Dibujar un círculo en la posición calculada
            #cv2.circle(img, (x, y), 3, (0, 234, 0), -1)  # Color rojo
            cv2.circle(img, (x-2, y-2), 3, (0, 0, 0), -1)  # Color rojo
        
        # Mostrar la constante k en la imagen
        #cv2.putText(img, f"k = {k:.2f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Mostrar la imagen
        cv2.imshow("Parametric Animation", img)
        #img = np.ones((width, height, 3), dtype=np.uint8) * 255
        
        # Incrementar el ángulo
        theta += theta_increment
        
        # Reiniciar theta si alcanza su valor máximo
        #if theta >= max_theta:
        #    theta = 0  # Reinicia la animación para que se repita

        # Pausar para ver la animación
        if cv2.waitKey(30) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
            break
    return img


# Crea 10 figuras geométricas con diferentes parámetros
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(100, 50, 3, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(120, 80, 4, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(80, 120, 2, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(90, 60, 6, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(110, 70, 5, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(130, 90, 7, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(70, 110, 3, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(140, 60, 4, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(150, 100, 5, 0.01, 10))
cv2.imshow("Parametric Animation", create_ecuation_parametrica_draw(60, 140, 6, 0.01, 10))



# Cerrar la ventana al finalizar
cv2.destroyAllWindows()
