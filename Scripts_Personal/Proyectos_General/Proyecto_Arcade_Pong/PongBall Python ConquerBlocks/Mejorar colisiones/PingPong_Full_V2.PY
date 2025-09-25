import tkinter as tk
from tkinter import messagebox
import random

# 🧩 1. Funciones defensivas externas

def verificar_aplastamiento_con_barra(ox1, ox2, oy1, oy2, bx1, bx2, by1, by2, dy):
    atrapado_por_suelo = oy2 >= 298 and dy > 0 and by1 < oy2 and ox2 > bx1 and ox1 < bx2
    atrapado_por_techo = oy1 <= 0 and dy < 0 and by2 > oy1 and ox2 > bx1 and ox1 < bx2
    return atrapado_por_suelo or atrapado_por_techo

def colision_con_barra(ox1, oy1, ox2, oy2, bx1, by1, bx2, by2, dy):
    """Verifica si la esfera colisiona con la barra, considerando dirección descendente."""
    if dy > 0 and oy2 >= by1 and ox2 >= bx1 and ox1 <= bx2:
        return True
    return False

# 🧩 2. Clase principal

class Simulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌌 Simulación Orbital Extendida")
        self.geometry("600x400")
        self.configure(bg="#0d0d1a")
        self.inicializar_estado()
        self.crear_canvas()
        self.crear_decorado()
        self.crear_objetos()
        self.crear_overlay()
        self.crear_controles()
        self.bind_eventos()
        self.after(500, self.actualizar)

    def inicializar_estado(self):
        self.estado = "activo"
        self.en_colision_letal = False
        self.vidas = 3
        self.teclas_activas = set()

    def crear_canvas(self):
        self.canvas = tk.Canvas(self, width=500, height=300, bg="white", highlightthickness=0)
        self.canvas.pack()

    def crear_decorado(self):
        for _ in range(60):
            x, y = random.randint(0, 500), random.randint(0, 250)
            self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="", tags="estrella")
        self.canvas.create_rectangle(0, 298, 500, 300, fill="#1a1a2e", outline="")
        for i in range(5):
            x = i * 120 + random.randint(-30, 30)
            self.canvas.create_polygon(x, 298, x+60, 240, x+120, 298,
                                       fill="#2c2f2f", outline="black")

    def crear_objetos(self):
        self.barra = self.canvas.create_rectangle(220, 260, 280, 270, fill="#0080FF", outline="")
        self.objeto = self.canvas.create_oval(240, 100, 260, 120, fill="lime", outline="")
        self.dx = random.choice([-1, 1]) * 5
        self.dy = random.choice([-1, 1]) * 5

    def crear_overlay(self):
        self.label_overlay = tk.Label(self.canvas, fg="white", bg="#1a1a2e",
                                      font=("Consolas", 9), justify="left")
        self.label_overlay.place(x=10, y=305)

    def crear_controles(self):
        self.slider = tk.Scale(self.canvas, from_=1, to=15, orient="horizontal",
                               bg="#1a1a2e", fg="white", troughcolor="#5c5c5c",
                               highlightthickness=0, length=100,
                               command=self.actualizar_velocidad)
        self.slider.set(5)
        self.slider.place(x=400, y=305)

        self.boton_pausa = tk.Button(self.canvas, text="⏸️ Pausar", command=self.pausar,
                                     bg="#333", fg="white", font=("Consolas", 9))
        self.boton_pausa.place(x=510, y=305)

        self.boton_salir = tk.Button(self.canvas, text="❌ Salir", command=self.confirmar_salida,
                                     bg="#333", fg="white", font=("Consolas", 9))
        self.boton_salir.place(x=510, y=335)

    def bind_eventos(self):
        self.bind("<KeyPress>", self.tecla_presionada)
        self.bind("<KeyRelease>", self.tecla_liberada)

    def actualizar(self):
        if self.estado != "activo":
            self.after(50, self.actualizar)
            return

        self.canvas.move(self.objeto, self.dx, self.dy)
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.objeto)
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)

        # 🧠 Colisión con barra
        if colision_con_barra(ox1, oy1, ox2, oy2, bx1, by1, bx2, by2, self.dy):
            self.dy *= -1
            self.canvas.move(self.objeto, 0, -10)
            print("[🟦] Rebote con barra detectado.")

        # 🧠 Colisión letal
        if verificar_aplastamiento_con_barra(ox1, ox2, oy1, oy2, bx1, bx2, by1, by2, self.dy):
            self.en_colision_letal = True
            self.vidas -= 1
            print(f"[💀] Aplastamiento letal. Vidas restantes: {self.vidas}")
            self.reiniciar_objeto()
            return

        # 🧠 Reaparición indebida
        if oy2 >= 298 and not self.en_colision_letal and by1 < oy2 and ox2 > bx1 and ox1 < bx2:
            self.vidas -= 1
            print(f"[⚠️] Fuga orbital detectada. Vidas restantes: {self.vidas}")
            self.reiniciar_objeto()
            return

        # 🧠 Rebote en bordes
        if ox1 <= 0 or ox2 >= 500:
            self.dx *= -1
        if oy1 <= 0 or oy2 >= 298:
            self.dy *= -1

        # 🧠 Movimiento por teclas
        if "Left" in self.teclas_activas:
            self.canvas.move(self.barra, -10, 0)
        if "Right" in self.teclas_activas:
            self.canvas.move(self.barra, 10, 0)

        # 🧠 Overlay técnico
        self.label_overlay.config(text=f"Vidas: {self.vidas} | Velocidad: {self.slider.get()}")

        # 🛑 Fin del juego
        if self.vidas <= 0:
            print("[🛑] Juego terminado. Sin vidas restantes.")
            self.estado = "terminado"
            messagebox.showinfo("Fin", "¡Has perdido todas tus vidas!")
            self.destroy()
            return

        # 🚀 Siguiente ciclo
        self.after(50, self.actualizar)

    def reiniciar_objeto(self):
        self.en_colision_letal = False
        self.canvas.coords(self.objeto, 240, 100, 260, 120)
        velocidad = self.slider.get()
        self.dx = random.choice([-1, 1]) * velocidad
        self.dy = random.choice([-1, 1]) * velocidad
        print(f"[🔄] Reinicio orbital. dx={self.dx}, dy={self.dy}")

    def pausar(self):
        if self.estado == "activo":
            self.estado = "pausado"
            print("[⏸️] Simulación pausada.")
        else:
            self.estado = "activo"
            print("[▶️] Simulación reanudada.")

    def confirmar_salida(self):
        respuesta = messagebox.askyesno("Confirmar salida", "¿Seguro que deseas salir?")
        if respuesta:
            print("[❌] Simulación finalizada por el usuario.")
            self.destroy()

    def tecla_presionada(self, evento):
        self.teclas_activas.add(evento.keysym)

    def tecla_liberada(self, evento):
        self.teclas_activas.discard(evento.keysym)

    def actualizar_velocidad(self, valor):
        velocidad = int(valor)
        self.dx = velocidad if self.dx >= 0 else -velocidad
        self.dy = velocidad if self.dy >= 0 else -velocidad
        print(f"[⚙️] Velocidad ajustada: dx={self.dx}, dy={self.dy}")

# 🚀 Ejecución principal

if __name__ == "__main__":
    app = Simulador()
    app.mainloop()
