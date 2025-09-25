import cv2

def listar_camaras():
    print("Buscando cámaras disponibles...")
    for i in range(2):  # Solo verifica índices 0 y 1
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Cámara detectada en índice {i}")
            cap.release()
        else:
            print(f"No hay cámara en índice {i}")

listar_camaras()
