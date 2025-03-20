from flask import render_template, Flask, request
import flask
import requests
import time

app = Flask(__name__)

@app.route("/index.html")
def redirect():
    return redirect("127.0.0.1"+"/", code=302)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form["name"] == "" and request.form["email"] == "" and request.form["classes"] == "": return render_template("index.html")
        name, email, gym_class, ip = request.form["name"], request.form["email"], request.form["classes"], request.environ["REMOTE_ADDR"]
        try:
            with open("log.txt", "r"):
                pass
        except FileNotFoundError:
            with open("log.txt", "x"):
                pass
        finally:
            with open("log.txt", "a") as file:
                file.write("{} | Name: {} Email: {} Class: {} IP: {}\n".format(time.strftime("%d/%m/%Y %H:%M:%S"), name, email, gym_class, ip))
    return render_template("index.html")

@app.route("/bookings")
def bookings():
    with open("log.txt", "r") as file:
        return flask.jsonify(file.readlines())