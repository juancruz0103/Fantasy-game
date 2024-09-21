import random

# Creamos las clases Heroe, Enemigo y Batalla para manejar la creación de los personajes y la batalla
class Heroe:
    def crear_heroe(nombre, ataque, vida):
        if ataque > 20:
            raise ValueError("El ataque no puede ser mayor a 20") # Lanzamos una excepción si el ataque es mayor a 20
        if vida > 200:
            raise ValueError("La vida no puede ser mayor a 200")  # Lanzamos una excepción si la vida es mayor a 200
        return {"nombre": nombre, "ataque": ataque, "vida": vida}

class Enemigo:
    def crear_enemigo(nombre, ataque, vida):
        return {"nombre": nombre, "ataque": ataque, "vida": vida}

class Batalla:
    def iniciar_batalla(heroe, enemigos):
        # Mostramos un mensaje de inicio de la batalla con la vida y ataque del héroe
        print(f"\nEl heroe {heroe['nombre']} inicia la batalla con {heroe['vida']} de vida y {heroe['ataque']} de ataque")
        for enemigo in enemigos:  # Iteramos sobre la lista de enemigos para pelear con cada uno
            print(f"\nUn {enemigo['nombre']} aparece")
            while heroe["vida"] > 0 and enemigo["vida"] > 0:
                enemigo["vida"] -= heroe["ataque"]
                if enemigo["vida"] > 0:
                    heroe["vida"] -= enemigo["ataque"]
            if heroe["vida"] > 0:
                heroe["vida"] += 30  # Recuperamos 30 de vida cada vez que derrotamos a un enemigo
                heroe["ataque"] += 5  # Aumentamos el ataque en 5 cada vez que derrotamos a un enemigo
                print(f"Has derrotado a {enemigo['nombre']} recuperas 30 de vida y aumentas tu ataque en 5")
            else:
                print(f"Has sido derrotado por el {enemigo['nombre']}")
                break

# Creamos un bucle infinito para que el juego se pueda jugar varias veces mientras el usuario asi lo desee
while True:

#Un mensajito de bienvenida o introducción al juego
    print("\nBienvenido al juego de aventuras de fantasia en donde competiras "
          "y tendras que superar diferentes enemigos para ganar la batalla final")

# Creamos el héroe por un input del usuario y manejamos las excepciones de los valores ingresados con un try-except
    while True:
        try:
            nombre_heroe = input("\nIngrese el nombre del heroe: ")
            ataque_heroe = int(input("Ingrese el ataque del heroe: "))
            vida_heroe = int(input("Ingrese la vida del heroe: "))
            heroe = Heroe.crear_heroe(nombre_heroe, ataque_heroe, vida_heroe)
            break
        except ValueError as e:
            print(e)

    # Creamos los enemigos a los que se enfrentará el héroe a traves de una lista
    enemigos = [
        Enemigo.crear_enemigo("Goblin", 5, 30),
        Enemigo.crear_enemigo("Orco", 10, 50),
        Enemigo.crear_enemigo("Troll", 15, 80),
        Enemigo.crear_enemigo("Dragon", 20, 100),
        Enemigo.crear_enemigo("Ropaloulista", 25, 200),
        Enemigo.crear_enemigo("Rey Demonio", 24, 250),
    ]

    # Iniciamos la batalla con los primeros 4 enemigos de la lista
    Batalla.iniciar_batalla(heroe, enemigos[:4])

    # Si el héroe sobrevive, pelea con uno de los dos últimos enemigos al azar que tendran el rol del enemigo final
    if heroe["vida"] > 0:
        enemigo_final = random.choice(enemigos[4:6]) # Elegimos un enemigo final al azar entre las dos ultimas posiciones de la lista
        print(f"\nUn {enemigo_final['nombre']} aparece para la batalla final")
        Batalla.iniciar_batalla(heroe, [enemigo_final])

    # Mostramos el resultado final de la batalla y si el héroe ganó o perdió
    if heroe["vida"] > 0:
        print("¡Felicidades! Has derrotado a todos los enemigos")
    else :
        print("¡Lo siento! Has sido derrotado por los enemigos")

    # Preguntamos al usuario si desea volver a jugar y si la respuesta es diferente de "si" salimos del bucle con un break
    respuesta_volver_jugar = input("\n¿Desea volver a jugar? (si/no): ")
    if respuesta_volver_jugar.lower() != "si": # Convertimos la respuesta a minúsculas para que no importe si es "Si" o "SI"
        print("\nGracias por jugar este maravilloso juego de aventuras")
        break