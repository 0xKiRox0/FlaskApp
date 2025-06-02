from app import app
from flask import render_template, jsonify
import random

@app.route("/") #Route for the homepage
def index():
    return render_template("index.html")

@app.route("/data") #API endpoint, return simulated (random) gauge data)
def data():
    value = random.randint(0, 2800)
    return jsonify({"value": value})