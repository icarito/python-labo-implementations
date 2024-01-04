import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_jugador = 0
    intentos_computadora = 0

    print("Bienvenido a Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. Intenta adivinarlo.")

    while True:
        # Turno del jugador
        intentos_jugador += 1
        intento_jugador = int(input("Tu turno. Ingresa tu número: "))
        
        if intento_jugador < numero_secreto:
            print("Muy bajo!")
        elif intento_jugador > numero_secreto:
            print("Muy alto!")
        else:
            print(f"¡Felicitaciones! Adivinaste el número en {intentos_jugador} intentos.")
            break

        # Turno de la computadora
        intentos_computadora += 1
        intento_computadora = random.randint(1, 100)

        print(f"Turno de la computadora: {intento_computadora}")

        if intento_computadora < numero_secreto:
            print("Muy bajo!")
        elif intento_computadora > numero_secreto:
            print("Muy alto!")
        else:
            print(f"¡La computadora adivinó el número en {intentos_computadora} intentos!")
            break

if __name__ == "__main__":
    adivina_el_numero()

