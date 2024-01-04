from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

class Player:
    def __init__(self, name):
        self.name = name

    def guess(self):
        raise NotImplementedError("Método guess debe ser implementado en subclases.")

class HumanPlayer(Player):
    def guess(self):
        try:
            return int(request.form['number'])
        except ValueError:
            return None

class ComputerPlayer(Player):
    def guess(self):
        return random.randint(1, 100)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = int(request.form['number'])
        guessed_number = int(request.form['guessed_number'])
        feedback = ""
        if guessed_number < number:
            feedback = "Muy bajo!"
        elif guessed_number > number:
            feedback = "Muy alto!"
        else:
            feedback = "¡Correcto! ¡Has adivinado el número!"
        return render_template('index.html', feedback=feedback)

    return render_template('index.html', feedback=None)

if __name__ == '__main__':
    app.run(debug=True)

