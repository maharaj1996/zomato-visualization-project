from flask import Flask,render_template,request
import sqlite3
import json
import pickle

app= Flask(__name__)






if __name__ == '__main__' :
    app.run(host="0.0.0.0", port= 5500)