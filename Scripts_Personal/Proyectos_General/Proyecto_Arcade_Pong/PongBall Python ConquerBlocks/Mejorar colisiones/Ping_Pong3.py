import tkinter as tk
import random

class Simulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌌 Simulación Orbital Extendida")
        self.geometry("500x400")
        self.configure(bg="#0d0d1a")

        self.score = 0
        self.teclas_activas = set()

        self.canvas = tk.Canvas(self, width=500, height=300, bg="#0d0d1a", highlightthickness=0)
        self.canvas.pack()

        self.zona_barra_y = 250
        self.canvas.create_line(0, self.zona_barra_y, 500, self.zona_barra_y, fill="#3c3f41")

        # 🌌 Fondo estelar
        for _ in range(80):
            x, y = random.randint(0, 500), random.randint(0, 250)
            self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="")

        # 🟦 Barra técnica
        self.barra = self.canvas.create_rectangle(220, 260, 280, 290, fill="deepskyblue", outline="")

        # 🟢 Objeto dinámico
        self.objeto = self.canvas.create_oval(240, 100, 260, 120, fill="lime", outline="")
        self.dx = random.choice([-1, 1]) * 5
        self.dy = random.choice([-1, 1]) * 5

        # 📊 Slider de velocidad
        self.slider = tk.Scale(self, from_=1, to=15, orient="horizontal", bg="#1a1a2e", fg="white",
                               troughcolor="#5c5c5c", highlightthickness=0, length=200,
                               command=self.actualizar_velocidad)
        self.slider.set(5)
        self.slider.place(x=150, y=310)

        # 🪐 Overlay técnico
        self.label_overlay = tk.Label(self, text="", fg="white", bg="#0d0d1a", font=("Consolas", 12))
        self.label_overlay.place(x=10, y=360)

        self.bind("<KeyPress>", self.tecla_presionada)
        self.bind("<KeyRelease>", self.tecla_liberada)

        self.actualizar()

    def actualizar(self):
        # 🎾 Mueve objeto
        self.canvas.move(self.objeto, self.dx, self.dy)
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.objeto)

        # 🧭 Rebote en bordes canvas
        if ox1 <= 0 or ox2 >= 500:
            self.dx *= -1
        if oy1 <= 0 or oy2 >= 300:
            self.dy *= -1

        # 🕹️ Mueve barra según teclas activas
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)
        desplazamiento = {"Left": (-5, 0), "Right": (5, 0), "Up": (0, -5), "Down": (0, 5),
                          "a": (-5, 0), "d": (5, 0), "w": (0, -5), "s": (0, 5)}
        for t in self.teclas_activas:
            dx, dy = desplazamiento.get(t, (0, 0))
            self.canvas.move(self.barra, dx, dy)

        # 🧱 Limita barra dentro del área
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)
        if bx1 < 0: self.canvas.move(self.barra, -bx1, 0)
        if bx2 > 500: self.canvas.move(self.barra, 500 - bx2, 0)
        if by1 < self.zona_barra_y: self.canvas.move(self.barra, 0, self.zona_barra_y - by1)
        if by2 > 300: self.canvas.move(self.barra, 0, 300 - by2)

        # 💥 Colisión completa con barra
        if ox2 > bx1 and ox1 < bx2 and oy2 > by1 and oy1 < by2:
            centro_objeto = ((ox1 + ox2) / 2, (oy1 + oy2) / 2)
            centro_barra = ((bx1 + bx2) / 2, (by1 + by2) / 2)
            angulo_x = centro_objeto[0] - centro_barra[0]
            angulo_y = centro_objeto[1] - centro_barra[1]

            # 🧠 Rebote según dirección de impacto
            self.dx = 5 if angulo_x > 0 else -5
            self.dy = 5 if angulo_y > 0 else -5

            color_nuevo = random.choice(["cyan", "magenta", "orange", "red", "deepskyblue"])
            self.canvas.itemconfig(self.barra, fill=color_nuevo)
            self.score += 1
        
        # 🧠 Al alcanzar cierto score, cambiar fondo
        if self.score >= 10 and not hasattr(self, "modo_galactico"):
            self.canvas.configure(bg="#1a0025")  # 🌌 Fondo más profundo
            self.canvas.delete("estrellas")
            for _ in range(100):
             x, y = random.randint(0, 500), random.randint(0, 250)
             estrella = self.canvas.create_oval(x, y, x+3, y+3, fill=random.choice(["white", "cyan", "violet", "deep pink"]), outline="")
             self.canvas.itemconfig(estrella, tags="estrellas")
             self.modo_galactico = True  # 🪐 Previene redibujar constantemente
             self.label_overlay.config(text=self.label_overlay.cget("text") + "   🚀 ¡Modo Galáctico Activado!")

        # 📋 Actualiza overlay técnico
        self.label_overlay.config(text=f"⚡ Velocidad: {abs(self.dx)} px/frame   💥 Score: {self.score}")

        self.after(30, self.actualizar)

    def actualizar_velocidad(self, valor):
        v = int(valor)
        self.dx = v if self.dx > 0 else -v
        self.dy = v if self.dy > 0 else -v

    def tecla_presionada(self, event):
        self.teclas_activas.add(event.keysym)

    def tecla_liberada(self, event):
        self.teclas_activas.discard(event.keysym)

# 🚀 Lanzamiento orbital
if __name__ == "__main__":
    Simulador().mainloop()
