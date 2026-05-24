from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return "Welcome to Home Page" 

@app.route('/admin5')
def Admin():
    return "Welcome to Admin Page"

@app.route('/user/<name>')
def User(name):
    if name == 'admin':
        return redirect(url_for('Admin')) 
    return f"user name is {name}"

@app.route('/gotogoogle1')
def Google():
    return redirect("https://www.google.com")

@app.route('/builturl')
def Builturl():
    result = url_for('Google')
    return f"my generated url or route is {result}"

app.run(debug=True)