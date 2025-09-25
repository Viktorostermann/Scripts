import mss
import mss.tools

with mss.mss() as sct:
    # Seleccionamos el monitor principal (índice 1 es el primer monitor)
    monitor = sct.monitors[1]
    screenshot = sct.grab(monitor)
    output = "captura_mss.png"
    mss.tools.to_png(screenshot.rgb, screenshot.size, output=output)
    print(f"Captura guardada como: {output}")