import tkinter as tk
import random

class Simulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🚀 Simulación Espacial con Colisiones")
        self.geometry("500x350")
        self.configure(bg="#0d0d1a")  # 💫 Fondo espacial

        self.canvas = tk.Canvas(self, width=500, height=300, bg="#0d0d1a", highlightthickness=0)
        self.canvas.pack()

        self.zona_barra_y = 250
        self.canvas.create_line(0, self.zona_barra_y, 500, self.zona_barra_y, fill="#3c3f41")

        # 🌌 Estrellas decorativas
        for _ in range(80):
            x, y = random.randint(0, 500), random.randint(0, 250)
            self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="")

        # 🟦 Barra controlable
        self.barra_color = "deepskyblue"
        self.barra = self.canvas.create_rectangle(220, 260, 280, 290, fill=self.barra_color, outline="")
        self.barra_dx = 0
        self.barra_dy = 0

        # 🟢 Objeto animado
        self.objeto = self.canvas.create_oval(240, 100, 260, 120, fill="lime", outline="")
        self.dx = random.choice([-1, 1]) * 5
        self.dy = random.choice([-1, 1]) * 5

        # 📊 Slider integrado
        self.slider = tk.Scale(self, from_=1, to=15, orient="horizontal", bg="#1a1a2e", fg="white",
                               troughcolor="#5c5c5c", highlightthickness=0, length=200,
                               command=self.actualizar_velocidad)
        self.slider.set(5)
        self.slider.place(x=150, y=310)

        # 🎮 Controles teclado
        self.bind("<KeyPress>", self.tecla_presionada)
        self.bind("<KeyRelease>", self.tecla_liberada)

        self.actualizar()

    def actualizar(self):
        # 🎾 Movimiento objeto
        self.canvas.move(self.objeto, self.dx, self.dy)
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.objeto)

        # 🧭 Rebote en bordes
        if ox1 <= 0 or ox2 >= 500:
            self.dx *= -1
        if oy1 <= 0 or oy2 >= self.zona_barra_y:
            self.dy *= -1

        # 🕹️ Movimiento barra
        self.canvas.move(self.barra, self.barra_dx, self.barra_dy)
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)

        if bx1 < 0 or bx2 > 500: self.barra_dx = 0
        if by1 < self.zona_barra_y or by2 > 300: self.barra_dy = 0

        # 💥 Colisión con barra
        if ox2 > bx1 and ox1 < bx2 and oy2 > by1 and oy1 < by2:
            self.dy = -abs(self.dy)
            nuevo_color = random.choice(["cyan", "magenta", "orange", "red", "deepskyblue"])
            self.canvas.itemconfig(self.barra, fill=nuevo_color)

        self.after(30, self.actualizar)

    def actualizar_velocidad(self, valor):
        v = int(valor)
        self.dx = v if self.dx > 0 else -v
        self.dy = v if self.dy > 0 else -v

    def tecla_presionada(self, event):
        if event.keysym in ("Left", "a"): self.barra_dx = -5
        if event.keysym in ("Right", "d"): self.barra_dx = 5
        if event.keysym in ("Up", "w"): self.barra_dy = -5
        if event.keysym in ("Down", "s"): self.barra_dy = 5

    def tecla_liberada(self, event):
        if event.keysym in ("Left", "Right", "a", "d"): self.barra_dx = 0
        if event.keysym in ("Up", "Down", "w", "s"): self.barra_dy = 0

# 🚀 Lanzamiento
if __name__ == "__main__":
    Simulador().mainloop()
