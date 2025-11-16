# Solicitar al usuario que ingrese su edad y género
edad = int(input('¿Cuál es tu edad? '))
genero = input('¿Cuál es tu género? (femenino/masculino) ').lower()

# Verificar si cumple con los requisitos
if 10 <= edad <= 12 and genero == 'femenino':
    print('Fuiste admitida!')
else:
    print('Lo siento, no podemos admitirte.')