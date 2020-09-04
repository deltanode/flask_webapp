from flask import Flask, render_template
import pyodbc

app = Flask(__name__, template_folder="templates")

db = pyodbc.connect('driver={SQL SERVER};' 'Server=DESKTOP-B6NTGC2\YOGESHPC;' 'UID=sa;' 'PWD=password;' 'Database=yogi_db;')
mycursor  = db.cursor()
mycursor.execute('select * from test')
row = [i for i in mycursor]

print()

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user")
def user():
    user_detail = [{"r_num":1,"name":"Amit"},{"r_num":2,"name":"Deep"},{"r_num":3,"name":"Rim"},
                   {"r_num":4,"name":"Dino"},{"r_num":5,"name":"Void"},{"r_num":6,"name":"Varun"},]
    return render_template("user.html", user_list=user_detail)

@app.route("/hello/<username>")
def hello(username):
    return 'Hello {0}'.format(username)

@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", name=username)

@app.route("/404")
def error404():
    return render_template("404.html")

@app.route("/database")
def database():
    return render_template("bootstrap.html", rows= row)

if __name__ == "__main__":
    app.run(debug=True)