import os
from reportlab.pdfgen import canvas

# Opcion 1: Ruta random destino para los PDFs automaticamente se utiliza guardar desde interfaz del usuario, PDFs o reportlab
'''Paso 1: Crear Archivo: 
   carpeta_destino = os.path.join(os.getcwd(), "Positivos", "PDFs")
   Paso 2: Crear Carpeta:
   os.makedirs(carpeta_destino, exist_ok=True) # Crea la carpeta si no existe Automatico
   Paso 3: Crear PDF:
   ruta_pdf = os.path.join(carpeta_destino, "test.pdf")'''

# Opcion 2: Ruta fija definida por usuario, por ejemplo:
# Paso 1: Crear Archivo: 
ruta_fija = r"C:\Users\vikto\Python_VsCode\A2-Scripts_Personal\Proyectos_General\Generador_de_PDF\Reportes_Modulo_Repor_Lab"

# Paso 2: Crear Carpeta si no existe:
os.makedirs(ruta_fija, exist_ok=True)

# Paso 3: Crear PDF, Ruta relativa a la ruta fija del PDF:
ruta_pdf = os.path.join(ruta_fija, "test.pdf") # Este codigo genera un PDF con el nombre "test.pdf"
 
#  Paso 4: Crear PDF con Reportlab y lal ibreria de Canvas
pdf = canvas.Canvas(ruta_pdf)
pdf.drawString(100, 750, "¡Reportlab está funcionando!") # .drawString(Hace que se pueda escribir texto en el PDF)
pdf.save()

#  Paso 5: Instruccion que pide Abrir el PDF en el explorador predeterminado de Windows (Solo Windows)
os.startfile(ruta_pdf) # Abrir el PDF en el explorador por defecto de Windows

#  Paso 6: Mostrar trazabilidad en consola: 
print("✅ PDF generado en:")
print(ruta_pdf)

# Instruccion que pide Abrir el archivo PDF en el explorador predeterminado de Linux y macOS
'''import subprocess
subprocess.run(["xdg-open", "test.pdf"])  # Linux
subprocess.run(["open", "test.pdf"])    # macOS'''
