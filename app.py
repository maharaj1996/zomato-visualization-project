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



@app.route('/contact', methods = ["GET","POST"])
def contactus():
    if request.method=='POST':
        name = request.form.get("name")
        email = request.form.get("email")
        country = request.form.get("country")
        state = request.form.get("state")
        message = request.form.get("message")
        print(name,email,country,state,message)
        conn = sqlite3.connect('contactus.db')
        cur = conn.cursor()
        cur.execute(f'''
        INSERT INTO CONTACT VALUES(
                    "{name}","{email}",
                    "{country}","{state}",
                    "{message}"
        )
        ''')
        conn.commit()
        return render_template('message.html')
    else:
        return render_template('contactus.html')






if __name__ == '__main__' :
    app.run(host="0.0.0.0", port= 5500)