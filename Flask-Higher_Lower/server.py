import random

from flask import Flask

app = Flask(__name__)
random_number = random.randint(9, 9)


@app.route('/')
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route(f'/guess/<int:number>')
def guess(number):
    if number == random_number:
        return ("<h1 style='color:red;'>You! Found me</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
    elif number > random_number:
        return ("<h1 style='color:blue;'>Too! High, Try again</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    else:
        return ("<h1 style='color:blue;'>Too! Low, Try again</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
