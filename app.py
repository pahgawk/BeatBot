from flask import Flask, render_template

from learn import Learn
from tomidi import toMidi

import json

MIDI_TEMP_PATH = 'output.mid'

app = Flask(__name__)
@app.route('/')
def server():
	return render_template("index.html")

@app.route('/music')
def music_function():
    learner = Learn()
    learner.loadFromFile()
    song = learner.getSong(getStartSequence())
    toMidi(song, MIDI_TEMP_PATH)

    return json.dumps(song)

@app.route('/train')
def train_function():
    learner = Learn()
    learner.train()
    learner.saveToFile()
    return server()

def getStartSequence():
    return [0, 7, 9, 0]

if __name__ == "__main__":
    app.run(debug = True)
