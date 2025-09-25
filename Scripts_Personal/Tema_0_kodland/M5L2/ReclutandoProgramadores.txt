edad = int(input('¿Cuántos años tienes? '))
exp = int(input('¿Cuántos años llevas programando? '))
horas = int(input('¿Cuántas horas puedes trabajar al día? '))
lenguaje = input('¿Qué lenguajes de programación conoces? (Python, C#, C++, otros) ').lower()
proyectos_videojuegos = int(input('¿Cuántos proyectos de videojuegos has desarrollado? '))
trabajo_equipo = input('¿Has trabajado en equipo? (sí/no) ').lower()

# Definimos las condiciones
condiciones = (
    edad >= 16 and 
    exp >= 3 and 
    horas >= 5 and 
    ('c#' in lenguaje or 'python' in lenguaje or 'c++' in lenguaje) and 
    proyectos_videojuegos > 0 and 
    trabajo_equipo == 'sí'
)

if condiciones:
    print("¡Felicitaciones, fuiste contratado!")
else:
    print('Lamentablemente no cumples con los requisitos')