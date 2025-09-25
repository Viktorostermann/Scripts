import cv2
import os
import datetime

# Directorio para guardar imágenes y videos
DIRECTORIO = "C:/Users/vikto/Python_VsCode/Capturas"
os.makedirs(DIRECTORIO, exist_ok=True)

# Configurar cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Configurar grabación de video
grabando = False
video_writer = None

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: No se pudo capturar el fotograma.")
        break

    cv2.imshow("Vista de cámara", frame)

    key = cv2.waitKey(1) & 0xFF
    
    # **Cerrar ventana**
    if key == ord('q'):
        break

    # **Capturar imagen**
    elif key == ord('c'):
        nombre_img = os.path.join(DIRECTORIO, f"captura_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        cv2.imwrite(nombre_img, frame)
        print(f"📸 Imagen guardada en {nombre_img}")

    # **Iniciar/Detener grabación de video**
    elif key == ord('v'):
        if not grabando:
            nombre_video = os.path.join(DIRECTORIO, f"video_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi")
            video_writer = cv2.VideoWriter(nombre_video, cv2.VideoWriter_fourcc(*"XVID"), 20, (frame.shape[1], frame.shape[0]))
            grabando = True
            print(f"🎥 Grabación iniciada: {nombre_video}")
        else:
            grabando = False
            video_writer.release()
            print("⏹ Grabación detenida.")

    # **Guardar fotogramas si está grabando**
    if grabando:
        video_writer.write(frame)

cap.release()
cv2.destroyAllWindows()
