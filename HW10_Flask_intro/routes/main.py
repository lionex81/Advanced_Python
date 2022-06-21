from app import app
from flask import render_template


@app.route("/")
def hello_world():
    a = "Hello, friend!"
    return render_template("index.html", variable=a)

@app.route("/add/<num1>/<num2>")
def adding(num1, num2):
    sum = int(num1) + int(num2)
    result = str(sum)
    return render_template("Adding.html", variable=result)

