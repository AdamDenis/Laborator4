# application.py
from flask import Flask, render_template

application = Flask(__name__)  # not `app = Flask(...)`

@application.route("/")
def hello():
    return render_template("index.html")
