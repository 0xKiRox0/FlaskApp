from app import app
from flask import render_template, jsonify
import random

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    value = random.randint(0, 100)
    return jsonify({"value": value})