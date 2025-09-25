import tkinter as tk

class BarraPong(tk.Canvas):
    def __init__(self, master=None, ancho=400, alto=150, velocidad=5):
        super().__init__(master, width=ancho, height=alto, bg="#1e1e1e", highlightthickness=0)
        self.pack()
        self.velocidad = velocidad
        self.direccion = 1  # Derecha inicialmente

        # 🎮 Crea barra gráfica
        self.barra = self.create_rectangle(10, 60, 60, 90, fill="deepskyblue", outline="")

        # 🚀 Inicia movimiento animado
        self.mover()

    def mover(self):
        self.move(self.barra, self.velocidad * self.direccion, 0)
        pos = self.coords(self.barra)

        # 🔁 Cambia dirección si alcanza bordes
        if pos[2] >= self.winfo_width() or pos[0] <= 0:
            self.direccion *= -1

        self.after(20, self.mover)

    def actualizar_velocidad(self, nueva):
        self.velocidad = nueva

class ControlVelocidad(tk.Toplevel):
    def __init__(self, master=None, callback=None, rango=(1, 20), valor_inicial=5):
        super().__init__(master)
        self.title("🛠️ Control de Velocidad")
        self.resizable(False, False)
        self.configure(bg="#2b2b2b")
        self.callback = callback

        # 📊 Slider técnico con overlay visual
        tk.Label(self, text=f"Velocidad inicial: {valor_inicial}", fg="white", bg="#2b2b2b").pack(pady=(10, 5))

        self.slider = tk.Scale(self, from_=rango[0], to=rango[1], orient="horizontal",
                               command=self.actualizar_valor, bg="#3c3f41", fg="white",
                               troughcolor="#5c5c5c", highlightthickness=0, length=200)
        self.slider.set(valor_inicial)
        self.slider.pack(padx=10, pady=(0, 10))

    def actualizar_valor(self, valor):
        valor_int = int(valor)
        if self.callback:
            self.callback(valor_int)

# 🧪 Integración técnica
if __name__ == "__main__":
    root = tk.Tk()
    root.title("🎮 Simulación Pong Controlado")
    root.geometry("400x200")
    root.configure(bg="#1e1e1e")

    barra_canvas = BarraPong(root)

    def recibir_velocidad(v):
        barra_canvas.actualizar_velocidad(v)

    # 🖱️ Panel flotante desacoplado
    panel = ControlVelocidad(master=root, callback=recibir_velocidad)

    root.mainloop()
