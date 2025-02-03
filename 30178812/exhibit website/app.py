import flask
import requests
import os

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("whatIremember.html")

@app.route("/thepagewitheverything")
def everything():
    return flask.render_template("everything.html")

@app.route("/thefile")
def file():
    with open("hidden_file.txt", "r") as secret:
        return flask.jsonify(secret.readlines())

@app.route("/favicon.ico")
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico")