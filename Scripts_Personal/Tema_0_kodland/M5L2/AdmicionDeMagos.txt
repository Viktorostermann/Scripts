#  Variables...
mago = input('¿Eres un mago (si o no)?')
edad = int(input('¿Cuantos años tienes?'))

#  Condiciones...
if mago == 'si' and edad >= 11 and edad <= 17:
    print("¡Felicitaciones, fuiste admitido!")
#  Copy + Paste para añadir "SI" y "Si" como opciones:
elif mago == 'Si' and edad >= 11 and edad <= 17:
    print("¡Felicitaciones, fuiste admitido!")
elif mago == 'SI' and edad >= 11 and edad <= 17:
    print("¡Felicitaciones, fuiste admitido!")

#  Else:
else:
    print("No puedes estudiar en Hogwarts, pero puedes aprender programacion en Kodland")