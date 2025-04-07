import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_schoolyard_retort():
    retorts = [
        "I know you are, but what am I?",
        "Your mom!",
        "No backsies!",
        "Takes one to know one!",
        "I'm rubber, you're glue, whatever you say bounces off me and sticks to you!",
        "Last one there is a rotten egg!",
        "Not uh!",
        "Yeah, well, double infinity no take-backs!",
        "Make me!",
        "Oh yeah? Prove it!",
        "Psych!",
        "Liar, liar, pants on fire!",
        "You and what army?",
        "Did too! Did not! Did too! Did not!",
        "Betcha can't catch me!"
    ]
    return random.choice(retorts)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_retort', methods=['POST'])
def get_retort():
    return jsonify({'response': get_schoolyard_retort()})

if __name__ == "__main__":
    app.run(debug=True)

