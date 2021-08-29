import requests
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

Admin = {
    "username": # write your username for login to app,
    "password": # write your password for login to app
}

Proxy = {
    # write your proxy for call api
}


def Responce():
    r = requests.get("https://api.coinbase.com/v2/prices/buy?currency=USD", proxies=Proxy)
    return r.json()


@app.route("/")
def index():
    """ this founction is home pages. """
    return render_template("home.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if not username:
        return "Error! Pleas enter your username"
    if not password:
        return "Error! Pleas enter your password"
    if not username and not password:
        return "Error! Pleas enter your username and password"
    if username == Admin["username"] and password == Admin["password"]:
        return render_template("admin.html", Responce=Responce())
    if username != Admin["username"] and password != Admin["password"]:
        return "Oh man you not did it Pleas try again! enter your username or password"
