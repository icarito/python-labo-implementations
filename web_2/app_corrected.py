from flask import Flask, render_template, request, session
from flask_session import Session
import random

app = Flask(__name__)

# Configura la extensión Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Las clases Player, HumanPlayer y ComputerPlayer se mantienen igual
class Player:
    def __init__(self, name):
        self.name = name

    def guess(self, secret_number):
        raise NotImplementedError("Método guess debe ser implementado en subclases.")

class HumanPlayer(Player):
    def guess(self, secret_number):
        try:
            return int(request.form['number'])
        except ValueError:
            return None

class ComputerPlayer(Player):
    def guess(self, secret_number):
        # Aquí puedes implementar una estrategia más inteligente si lo deseas
        return random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 100)

    secret_number = session['secret_number']

    player = HumanPlayer("Jugador")
    computer = ComputerPlayer("Computadora")

    feedback = ""

    if request.method == 'POST':
        guessed_number = player.guess(secret_number)
        computer_guess = computer.guess(secret_number)

        if guessed_number < secret_number:
            feedback = "Muy bajo!"
        elif guessed_number > secret_number:
            feedback = "Muy alto!"
        else:
            feedback = "¡Correcto! ¡Has adivinado el número!"

        return render_template('index.html', feedback=feedback, secret_number=secret_number, computer_guess=computer_guess)

    return render_template('index.html', feedback=feedback, secret_number=secret_number, computer_guess=None)

if __name__ == '__main__':
    app.run(debug=True)

