import tkinter as tk
from tkinter import messagebox
import random
import pygame

# 💥 Verificación de aplastamiento letal (solo techo o suelo, según dirección)
def verificar_aplastamiento_con_barra(ox1, ox2, oy1, oy2, bx1, bx2, by1, by2, dy):
    atrapado_por_suelo = oy2 >= 298 and dy > 0 and by1 < oy2 and ox2 > bx1 and ox1 < bx2
    atrapado_por_techo = oy1 <= 0 and dy < 0 and by2 > oy1 and ox2 > bx1 and ox1 < bx2
    return atrapado_por_suelo or atrapado_por_techo

class Simulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🌌 Simulación Orbital Extendida")
        self.geometry("600x400")
        self.configure(bg="#0d0d1a")

        # 🧠 Estados internos
        self.en_colision_letal = False
        self.estado = "activo"
        self.tiempo_reinicio = 0

        # 📊 Variables de juego
        self.score = 0
        self.vidas = 3
        self.teclas_activas = set()
        self.fragmentos_explosion = []

        # 🎨 Canvas principal
        self.canvas = tk.Canvas(self, bg="#0d0d1a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # 🌌 Fondo estelar
        for _ in range(60):
            x, y = random.randint(0, 500), random.randint(0, 250)
            self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="", tags="estrella")

        # 🏔️ Suelo y montañas
        self.canvas.create_rectangle(0, 298, 500, 300, fill="#1a1a2e", outline="")
        for i in range(5):
            x = i * 120 + random.randint(-30, 30)
            self.canvas.create_polygon(x, 298, x+60, 240, x+120, 298,
                                       fill="#2c2f2f", outline="black")

        # 🟦 Barra de control
        self.barra = self.canvas.create_rectangle(220, 260, 280, 270, fill="#0080FF", outline="")

        # 🟢 Esfera orbital
        self.objeto = self.canvas.create_oval(240, 100, 260, 120, fill="lime", outline="")
        self.dx = random.choice([-1, 1]) * 5
        self.dy = random.choice([-1, 1]) * 5
        self.modo_espacial = False

        # 📊 Overlay técnico
        self.label_overlay = tk.Label(self.canvas, fg="white", bg="#1a1a2e",
                                      font=("Consolas", 9), justify="left")
        self.label_overlay.place(x=10, y=305)

        # 🎚️ Control de velocidad
        self.slider = tk.Scale(self.canvas, from_=1, to=15, orient="horizontal",
                               bg="#1a1a2e", fg="white", troughcolor="#5c5c5c",
                               highlightthickness=0, length=100,
                               command=self.actualizar_velocidad)
        self.slider.set(5)
        self.slider.place(x=400, y=305)

        # 🎮 Eventos de teclado
        self.bind("<KeyPress>", self.tecla_presionada)
        self.bind("<KeyRelease>", self.tecla_liberada)

        # 🚀 Inicio del ciclo de actualización
        self.actualizar()

    # 🧠 Registro técnico del aplastamiento
    def mostrar_aplastamiento_detectado(self, centro, ox1, ox2, oy1, oy2, bx1, bx2, by1, by2):
        if getattr(self, "_aplastamiento_en_proceso", False):
            print("🔁 Evento ignorado: detección en curso")
            return
        self._aplastamiento_en_proceso = True

        try:
            mensaje = f"💀 Aplastamiento detectado en ({centro[0]:.0f}, {centro[1]:.0f})"
            coordenadas = (
                f"🟠 Objeto: x=({ox1:.0f}-{ox2:.0f}), y=({oy1:.0f}-{oy2:.0f})\n"
                f"🔵 Barra:  x=({bx1:.0f}-{bx2:.0f}), y=({by1:.0f}-{by2:.0f})"
            )
            print(mensaje)
            print(coordenadas)
        except Exception as e:
            print(f"[Error] Fallo en el manejo del aplastamiento: {e}")
        finally:
            self._aplastamiento_en_proceso = False

    def tecla_presionada(self, event):
        self.teclas_activas.add(event.keysym)

    def tecla_liberada(self, event):
        self.teclas_activas.discard(event.keysym)

    # 🎨 Animación de color en la barra
    def animar_color_barra(self, colores, pasos=10, delay=30):
        actual = self.canvas.itemcget(self.barra, "fill")
        for i in range(pasos):
            nuevo = random.choice(colores)
            self.after(i * delay, lambda c=nuevo: self.canvas.itemconfig(self.barra, fill=c))

    # 💥 Generación de explosión visual
    def generar_explosion_suave(self, x, y):
        self.fragmentos_explosion.clear()
        for _ in range(20):
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            color = random.choice(["orange", "red", "yellow", "white"])
            frag = self.canvas.create_oval(x+dx, y+dy, x+dx+5, y+dy+5, fill=color, outline="")
            self.fragmentos_explosion.append(frag)
        self.after(300, self.borrar_explosion)

    def borrar_explosion(self):
        for f in self.fragmentos_explosion:
            self.canvas.delete(f)
        self.fragmentos_explosion.clear()

    # 💥 Reinicio defensivo tras colisión letal
    def perder_vida(self, centro):
        self.dy = 0
        self.dx = 0
        self.estado = "reiniciando"
        self.tiempo_reinicio = pygame.time.get_ticks()

        self.en_colision_letal = True
        self.vidas -= 1
        self.generar_explosion_suave(*centro)
        self.canvas.coords(self.objeto, 240, 100, 260, 120)
        self.dx = random.choice([-1, 1]) * 5
        self.dy = -5
        self.animar_color_barra(["#FF4444", "#FF8800", "#FFCC00"])

        if self.vidas == 0:
            continuar = messagebox.askyesno("💥 Juego terminado", "¿Deseas volver a jugar?")
            if continuar:
                self.vidas = 3
                self.score = 0
                self.dx = 5
                self.dy = 5
                self.modo_espacial = False
                self.canvas.configure(bg="#0d0d1a")
                self.canvas.delete("estrella")
                for _ in range(60):
                    x, y = random.randint(0, 500), random.randint(0, 250)
                    self.canvas.create_oval(x, y, x+2, y+2, fill="white", outline="", tags="estrella")
            else:
                self.destroy()

    # 🔄 Ciclo principal de actualización
    def actualizar(self):
        if self.estado == "reiniciando":
            if pygame.time.get_ticks() - self.tiempo_reinicio > 1000:
                self.reiniciar_posicion()
                self.estado = "activo"
            return

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        self.validar_posicion_esfera()
        self.canvas.move(self.objeto, self.dx, self.dy)

        ox1, oy1, ox2, oy2 = self.canvas.coords(self.objeto)
        centro = ((ox1 + ox2) / 2, (oy1 + oy2) / 2)
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)

        # 🧠 Verificación de colisión letal
        if not self.modo_espacial and not self.en_colision_letal and verificar_aplastamiento_con_barra(
            ox1, ox2, oy1, oy2, bx1, bx2, by1, by2, self.dy):
            self.en_colision_letal = True
            self.perder_vida(centro)
            self.mostrar_aplastamiento_detectado(centro, ox1, ox2, oy1, oy2, bx1, bx2, by1, by2)
            return

        self.actualizar_overlay()
        self.en_colision_letal = False

        if self.winfo_exists():
            self.after(20, self.actualizar)

        # ↔️ Rebote en bordes
        if ox1 <= 0 or ox2 >= canvas_width:
            self.dx *= -1
        if oy1 <= 0 or oy2 >= 298:
            self.dy *= -1

        # 🎮 Movimiento de barra por teclado
        teclas = {
            "Left": (-5, 0), "Right": (5, 0), "Up": (0, -5), "Down": (0, 5),
            "a": (-5, 0), "d": (5, 0), "w": (0, -5), "s": (0, 5)
        }
        for t in self.teclas_activas:
            dx, dy = teclas.get(t, (0, 0))
            self.canvas.move(self.barra, dx, dy)

        # 🧱 Defensa contra fuga de barra
        bx1, by1, bx2, by2 = self.canvas.coords(self.barra)
        if bx1 < 0: self.canvas.move(self.barra, -bx1, 0)
        if bx2 > canvas_width: self.canvas.move(self.barra, canvas_width - bx2, 0)
        if by1 < 0: self.canvas.move(self.barra, 0, -by1)
        if by2 > 298: self.canvas.move(self.barra, 0, 298 - by2)

        # 🧠 Rebote por contacto con barra
        if not self.en_colision_letal and ox2 > bx1 and ox1 < bx2 and oy2 > by1 and oy1 < by2:
            angulo_x = centro[0] - ((bx1 + bx2) / 2)
            angulo_y = centro[1] - ((by1 + by2) / 2)
            self.dx = 5 if angulo_x > 0 else -5
            self.dy = 5 if angulo_y > 0 else -5
            self.animar_color_barra(["#0070C0", "#0050A0", "#0066CC"])
            self.score += 1

        # 🌌 Cambio de modo espacial
        if self.score >= 5 and not self.modo_espacial:
            self.canvas.configure(bg="#110014")
            self.canvas.delete("estrella")
            for _ in range(100):
                x, y = random.randint(0, canvas_width), random.randint(0, canvas_height - 100)
                self.canvas.create_oval(x, y, x+3, y+3,
                    fill=random.choice(["white", "violet", "deep pink"]),
                    outline="", tags="estrella")
            self.modo_espacial = True

    # 📊 Actualización del overlay técnico
    def actualizar_overlay(self):
        canvas_height = self.canvas.winfo_height()
        vidas_iconos = " ".join(["🟢" if i < self.vidas else "⚫" for i in range(3)])
        self.label_overlay.config(
            text=f"{vidas_iconos}\n⚡ Velocidad: {abs(self.dx)} px/frame\n💥 Score: {self.score}"
        )
        self.label_overlay.place(x=10, y=canvas_height - 90)

    # 🎚️ Ajuste de velocidad desde slider
    def actualizar_velocidad(self, valor):
        velocidad = int(valor)
        self.dx = velocidad if self.dx > 0 else -velocidad
        self.dy = velocidad if self.dy > 0 else -velocidad

    # 🧱 Defensa contra desaparición de esfera
    def validar_posicion_esfera(self):
        if not self.canvas.find_withtag(self.objeto):
            return
        ox1, oy1, ox2, oy2 = self.canvas.coords(self.objeto)
        fuera = ox2 < 0 or ox1 > self.canvas.winfo_width() or oy2 < 0 or oy1 > 298
        if fuera:
            self.canvas.coords(self.objeto, 240, 100, 260, 120)
            self.dx = random.choice([-1, 1]) * 5
            self.dy = random.choice([-1, 1]) * 5
            self.animar_color_barra(["#FF4444", "#FF8800", "#FFCC00"])

    # 🔁 Reinicio tras colisión letal
    def reiniciar_posicion(self):
        self.canvas.coords(self.objeto, 240, 100, 260, 120)
        self.dx = random.choice([-1, 1]) * 5
        self.dy = random.choice([-1, 1]) * 5
        self.animar_color_barra(["#44FF44", "#88FF88", "#AAFFAA"])

# 🧠 Cierre de clase y ejecución principal
if __name__ == "__main__":
    app = Simulador()
    app.mainloop()
