from flask import Flask,render_template,request
import sqlite3
import json
import pickle


app= Flask(__name__)


@app.route('/')
def homepage():
    return render_template("home.html")

@app.route("/restaurants")
def restaurant():
   return render_template("restaurant.html") 


if __name__ == '__main__' :
    app.run(host="0.0.0.0", port= 5500)