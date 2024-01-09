import random

class Player:
    def __init__(self, name):
        self.name = name

    def guess(self):
        raise NotImplementedError("Método guess debe ser implementado en subclases.")

    def feedback(self, feedback):
        print(f"{self.name}: {feedback}")


class HumanPlayer(Player):
    def guess(self):
        try:
            return int(input(f"{self.name}, ingresa tu número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            return self.guess()


class ComputerPlayer(Player):
    def guess(self):
        return random.randint(1, 100)


def adivina_el_numero(jugador, computadora):
    numero_secreto = random.randint(1, 100)

    print("Bienvenido a Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina!")

    while True:
        # Turno del jugador humano
        intento_jugador = jugador.guess()
        if intento_jugador < numero_secreto:
            jugador.feedback("Muy bajo!")
        elif intento_jugador > numero_secreto:
            jugador.feedback("Muy alto!")
        else:
            print(f"¡Felicitaciones, {jugador.name}! Adivinaste el número.")
            break

        # Turno de la computadora
        intento_computadora = computadora.guess()
        if intento_computadora < numero_secreto:
            computadora.feedback("Muy bajo!")
        elif intento_computadora > numero_secreto:
            computadora.feedback("Muy alto!")
        else:
            print("¡La computadora ha adivinado el número!")
            break


if __name__ == "__main__":
    nombre_jugador = input("Ingresa tu nombre: ")
    jugador = HumanPlayer(nombre_jugador)
    computadora = ComputerPlayer("Computadora")
    adivina_el_numero(jugador, computadora)

