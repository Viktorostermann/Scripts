import tkinter as tk
import datetime

class ControlVelocidad(tk.Toplevel):
    def __init__(self, master=None, callback=None, rango=(0, 100), valor_inicial=50):
        super().__init__(master)
        self.title("🛠️ Panel de Velocidad")
        self.resizable(False, False)
        self.callback = callback
        self.rango = rango

        # 🎯 Posicionamiento flotante y desacoplado respecto a la ventana principal
        self.geometry("+{}+{}".format(master.winfo_rootx()+50, master.winfo_rooty()+50))
        self.configure(bg="#2b2b2b")

        # 🖼️ Etiqueta principal del valor actual
        self.label_valor = tk.Label(self, text=f"Velocidad: {valor_inicial}", fg="white", bg="#2b2b2b")
        self.label_valor.pack(pady=(10, 5))

        # 📊 Slider interactivo técnico
        self.slider = tk.Scale(
            self, from_=rango[0], to=rango[1], orient="horizontal",
            command=self.actualizar_valor, bg="#3c3f41", fg="white",
            troughcolor="#5c5c5c", highlightthickness=0, length=200
        )
        self.slider.set(valor_inicial)
        self.slider.pack(padx=10, pady=(0, 10))

        # 🔍 Overlay de estado visual (dentro/fuera del rango óptimo)
        self.overlay_estado = tk.Label(self, text="", fg="yellow", bg="#2b2b2b")
        self.overlay_estado.pack()

    def actualizar_valor(self, valor):
        valor_int = int(valor)
        self.label_valor.config(text=f"Velocidad: {valor_int}")
        if self.callback:
            self.callback(valor_int)

        # 📝 Registro automático en log visual
        self.registrar_log(valor_int)

        # ⚠️ Indicador visual de rango óptimo
        if valor_int < 20 or valor_int > 80:
            self.overlay_estado.config(text="⚠️ Valor fuera del rango óptimo")
        else:
            self.overlay_estado.config(text="✅ Velocidad dentro del rango ideal")

    def registrar_log(self, cambio):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("log_velocidad.txt", "a") as f:
            f.write(f"{timestamp} - Velocidad ajustada a: {cambio}\n")

# 💡 Ejemplo de uso
if __name__ == "__main__":
    def recibir_velocidad(v):
        print(f"📈 Velocidad ajustada a: {v}")

    root = tk.Tk()
    root.withdraw()  # 🧼 Oculta ventana principal para uso como panel desacoplado
    panel = ControlVelocidad(master=root, callback=recibir_velocidad)
    panel.mainloop()
