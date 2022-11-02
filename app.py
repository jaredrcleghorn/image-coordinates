from flask import Flask

app = Flask(__name__)


@app.route("/")
def image_coordinates():
    return "hello, image coordinates"
