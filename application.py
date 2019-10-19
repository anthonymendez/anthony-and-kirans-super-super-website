from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Index Page"

@app.route("/hello")
def hello():
    return "Hello World!"
