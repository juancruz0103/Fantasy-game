class Heroe:
    def crear_heroe(nombre, ataque, vida):
        if ataque > 20:
            print("El ataque no puede ser mayor a 20") #No esta funcionando el mensaje de error simplemente lo ignora
        if vida > 200:
            print("La vida no puede ser mayor a 200") #No esta funcionando el mensaje de error simplemente lo ignora
        return {"nombre": nombre, "ataque": ataque, "vida": vida}


class Enemigo:
    def crear_enemigo(nombre, ataque, vida):
        return {"nombre": nombre, "ataque": ataque, "vida": vida}


class Batalla:
    def iniciar_batalla(heroe, enemigos):
        victorias = 0
        for enemigo in enemigos:
            print(f"Un {enemigo['nombre']} aparece")
            while heroe["vida"] > 0 and enemigo["vida"] > 0:
                enemigo["vida"] -= heroe["ataque"]
                if enemigo["vida"] > 0:
                    heroe["vida"] -= enemigo["ataque"]
            if heroe["vida"] > 0:
                victorias += 1
                heroe["vida"] += 30 # Recuperamos 30 de vida
                heroe["ataque"] += 5 # Aumentamos el ataque en 5
                print(f"Has derrotado a {enemigo['nombre']} recuperas 30 de vida y aumentas tu ataque en 5")
            else:
                print(f"Has sido derrotado por el {enemigo['nombre']}")
                break
        if heroe["vida"] > 0:
            print(f"Has ganado {victorias} batallas")

        else:
            print(f"Has perdido la batalla con {victorias} victorias")


# Creamos el heroe
nombre_heroe = input("Ingrese el nombre del heroe: ")
ataque_heroe = int(input("Ingrese el ataque del heroe: "))
vida_heroe = int(input("Ingrese la vida del heroe: "))
heroe = Heroe.crear_heroe(nombre_heroe, ataque_heroe, vida_heroe)

# Creamos los enemigos¿
enemigos = [
    Enemigo.crear_enemigo("Goblin", 5, 30),
    Enemigo.crear_enemigo("Orco", 10, 50),
    Enemigo.crear_enemigo("Troll", 15, 80),
    Enemigo.crear_enemigo("Ropaloulista", 25, 200),
    Enemigo.crear_enemigo("Rey Demonio", 24, 250),
]

# Iniciamos la batalla
Batalla.iniciar_batalla(heroe, enemigos)