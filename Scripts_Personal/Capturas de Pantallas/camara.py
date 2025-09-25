import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Cámara integrada funcionando correctamente en índice 0")
    cap.release()
else:
    print("Error al acceder a la cámara, revisa controladores.")
