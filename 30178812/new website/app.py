import flask
import requests

app = flask.Flask(__name__)

@app.route("/index.html")
def redirect():
    return redirect("127.0.0.1"+"/", code=302)

@app.route("/", methods=["GET", "POST"])