'''
ENCRIPTACIÓN ROT13:
El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
catalán la ”Ç”, en alemán la ”ß”, etc.).
Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.

[a,b,c,d,e,f,g,h,i,j,k,l,m]     [H, O, L, A]

            ROT13

[n,o,p,q,r,s,t,u,v,w,x,y,z]     [U, B, Y, N]
'''
'''alfabeto = "abcdefghijklmnopqrstuvwxyz"
#alfabeto_mayusculas = alfabeto.upper()

# --- Se debe definir el alfabeto en listas en lugar de tuplas hay que corregir esto --- #
#alfabeto = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
alfabeto_mayusculas = []

for letra in alfabeto:
    alfabeto_mayusculas.append(letra.upper())

mensaje = input("Introduce el mensaje a encriptar: ")
mensaje = mensaje.lower()
#mensaje = "hola"
mensaje_comparar = input("Introduce el mensaje de comparacion: ")
mensaje_cifrado = ""

# --- recorremos cada una de las letras del mensaje
for char in mensaje:
    # Comprobamos si la letra es minuscula
    if char in alfabeto:
        # recorremos cada una de las letras del alfabeto
        for i in range(len(alfabeto)):
            # cuando encuentre la letra guardo el indice
            if char == alfabeto[i]:
                char_indice = i
            
                # Si la letra esta en la segunda mitad del alfabeto
                if char_indice + 13 >=26: 
                #restamos 26 para que al sumar 13 vuelva al principio del alfabeto nuevamente
                   #char_indice = char_indice -26
                # El nuevo indice cifrado sera el indice antiguo o inicial + 13
                   nuevo_indice = char_indice + 13 % 26
                else:
                   nuevo_indice = char_indice + 13
                #Accedemos a la letra cifrada del alfabeto por el indice cifrado
                   letra_cifrada = alfabeto[nuevo_indice]
                # Añadimos la letra cifrada al mensaje cifrado        
                   mensaje_cifrado = mensaje_cifrado + letra_cifrada

    elif char in alfabeto_mayusculas:
        # Alfabeto Mayusculas recorremos cada una de las letras del mensaje
        for char in mensaje:
            # recorremos cada una de las letras del alfabeto
            for i in range(len(alfabeto_mayusculas)):
                # cuando encuentre la letra guardo el indice
                if char == alfabeto_mayusculas[i]:
                   char_indice = i
                   #print("Indice inicial", char_indice)

                   # Si la letra esta en la segunda mitad del alfabeto
                   if char_indice + 13 >=26:
                      char_indice = char_indice -26

                   # El nuevo indice cifrado sera el indice antiguo o inicial + 13
                   nuevo_indice = char_indice + 13
                   # Accedemos a la letra cifrada del alfabeto por el indice cifrado
                   letra_cifrada = alfabeto_mayusculas[nuevo_indice]
            # Añadimos la letra cifrada al mensaje cifrado
            mensaje_cifrado = mensaje_cifrado + letra_cifrada
           
else:
    mensaje_cifrado = mensaje_cifrado + char

if len(mensaje_cifrado) == mensaje_comparar:
    print(f"Los Mensaje  {mensaje_cifrado} y {mensaje_comparar} son una encriptacion ROT13")  
else:
    print(f"Los Mensaje {mensaje_cifrado} y {mensaje_comparar} no son una encriptacion espejo")'''

# Definimos el alfabeto en listas en lugar de tuplas
alfabeto = list("abcdefghijklmnopqrstuvwxyz")
alfabeto_mayusculas = [letra.upper() for letra in alfabeto]

# Pedimos el mensaje a cifrar
mensaje = input("Introduce el mensaje a encriptar: ").lower()
mensaje_comparar = input("Introduce el mensaje de comparación: ")
mensaje_cifrado = ""

# Recorremos cada carácter del mensaje
for char in mensaje:
    if char in alfabeto:  # Si es una letra minúscula
        char_indice = alfabeto.index(char)
        nuevo_indice = (char_indice + 13) % 26  # Asegurar que rotamos correctamente
        mensaje_cifrado += alfabeto[nuevo_indice]
        
    elif char in alfabeto_mayusculas:  # Si es una letra mayúscula
        char_indice = alfabeto_mayusculas.index(char)
        nuevo_indice = (char_indice + 13) % 26
        mensaje_cifrado += alfabeto_mayusculas[nuevo_indice]

    else:
        mensaje_cifrado += char  # Si no es una letra, lo dejamos igual

# Comprobamos si el mensaje cifrado coincide con el mensaje de comparación
if mensaje_cifrado == mensaje_comparar:
    print(f"Los mensajes '{mensaje}' y '{mensaje_comparar}' son una encriptación ROT13")
else:
    print(f"Los mensajes '{mensaje}' y '{mensaje_comparar}' no son una encriptación espejo")
