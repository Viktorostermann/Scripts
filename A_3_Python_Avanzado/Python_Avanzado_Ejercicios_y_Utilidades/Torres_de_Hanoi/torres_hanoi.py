''' Ejercicio que Emula el comportamiento de
las torres de Hanoi (Towers of Hanoi). '''

import random

class TorreHanoi:
    def __init__(self, Num_Discos, Torre_A, Torre_B, Torre_C):
        self.Num_Discos = Num_Discos

        # Guardamos los nombres de las torres
        self.Torre_A = Torre_A
        self.Torre_B = Torre_B
        self.Torre_C = Torre_C

        # Seleccionamos aleatoriamente la torre de inicio
        self.torre_inicial = random.choice([Torre_A, Torre_B, Torre_C])

        # Las otras dos torres se asignan como destino y auxiliar
        torres_restantes = [t for t in [Torre_A, Torre_B, Torre_C] if t != self.torre_inicial]
        self.torre_destino, self.torre_aux = torres_restantes

        # Inicializamos las torres como listas (pilas)
        self.torres = {
            self.Torre_A: [],
            self.Torre_B: [],
            self.Torre_C: []
        }

        # Insertamos los discos en la torre inicial elegida al azar
        self.torres[self.torre_inicial] = list(range(Num_Discos, 0, -1))
        print("")
        print(f"🎲 Torre inicial elegida al azar: {self.torre_inicial}")
        print("")
        # Llamada inicial al método recursivo
        self.resolver(self.Num_Discos, self.torre_inicial, self.torre_destino, self.torre_aux)

    def mover(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        print(f'Mover disco {disco} desde la torre {origen} hasta la torre {destino}')

        # Explicación del estado actual de las torres
        print("📌 Estado actual de las torres:")
        for nombre, pila in self.torres.items():
            print(f"   Torre {nombre}: {len(pila)} discos -> {pila}")
        print("--------------------------------------------------")

    def resolver(self, n, origen, destino, auxiliar):
        ''' Método recursivo que resuelve las Torres de Hanoi '''
        if n == 1:
            self.mover(origen, destino)
        else:
            self.resolver(n - 1, origen, auxiliar, destino)
            self.mover(origen, destino)
            self.resolver(n - 1, auxiliar, destino, origen)

    def __str__(self):
        resumen = (f'Numero de Discos: {self.Num_Discos}\n'
                   f'Torre {self.Torre_A}: {len(self.torres[self.Torre_A])} discos -> {self.torres[self.Torre_A]}\n'
                   f'Torre {self.Torre_B}: {len(self.torres[self.Torre_B])} discos -> {self.torres[self.Torre_B]}\n'
                   f'Torre {self.Torre_C}: {len(self.torres[self.Torre_C])} discos -> {self.torres[self.Torre_C]}')
        return resumen

if __name__ == '__main__':
    print("")
    print('TORRES DE HANOI 🏛️')
    print('-------------------')
    print("")
    Num_Discos = int(input('Ingrese el numero de discos: '))
    print("")
    Torre_A = input('Nombre de la primera torre: ')
    print("")
    Torre_B = input('Nombre de la segunda torre: ')
    print("")
    Torre_C = input('Nombre de la tercera torre: ')
    
    print("")
    Torre_Hanoi = TorreHanoi(Num_Discos, Torre_A, Torre_B, Torre_C)
    print("\n")
    print('🚀 Resolviendo...')
    print("")
    print('\n📊 Estado final de las torres:')
    print("--------------------------------------------------")
    print(Torre_Hanoi)
    print("--------------------------------------------------")
    print('\n')

    input('Presiona enter para salir...')
    print("")