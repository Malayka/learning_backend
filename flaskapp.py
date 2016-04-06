from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi!"

@app.route("/hi")
def cantbe():
    return "What's up, bro?"


@app.route("/not_much")
def image():
    return send_file("vatrushka.jpg", mimetype='image/png')