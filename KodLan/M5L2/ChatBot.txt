movies = []

def show_movies():
    if not movies:
        print("No hay películas en la lista.")
    else:
        print("Películas en la lista:")
        for i, movie in enumerate(movies, start=1):
            print(str(i) + ". " + movie)

def add_movie():
    movie = input("Ingresa el nombre de la película que quieres agregar: ")
    movies.append(movie)
    print("'" + movie + "' ha sido añadida a la lista.")

def remove_movie():
    show_movies()
    if movies:
        try:
            choice = int(input("Ingresa el número de la película que has visto y deseas eliminar: "))
            if 1 <= choice <= len(movies):
                removed_movie = movies.pop(choice - 1)
                print("'" + removed_movie + "' ha sido eliminada de la lista.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor ingresa un número válido.")

def suggest_movie():
    if movies:
        print("Te sugiero ver: " + movies[0])  
    else:
        print("No tienes películas en la lista para sugerir.")

def chatbot():
    while True:
        print("\nComandos disponibles:")
        print("output - Muestra la lista de películas")
        print("add - Agregar nueva película")
        print("remove - Eliminar película vista")
        print("exit - Salir del programa")
        print("suggest - Sugerir una película")

        command = input("Escribe un comando: ").lower()

        if command == "output":
            show_movies()
        elif command == "add":
            add_movie()
        elif command == "remove":
            remove_movie()
        elif command == "suggest":
            suggest_movie()
        elif command == "exit":
            print("¡Hasta luego!")
            break
        else:
            print("Comando no reconocido. Por favor, ingresa un comando válido.")
chatbot()