from flask import Flask

app = Flask(__name__)

#static route
@app.route('/home')
def Home():
    return "Welcome to Home Page" # http://127.0.0.1:5000/home

@app.route('/home1')
def Home1():
    return "Welcome to Home Page 1" # http://127.0.0.1:5000/home1

@app.route('/about')
def About():
    return "Welcome to About Page" # http://127.0.0.1:5000/about

# dynamic route
@app.route('/<name>')
def Course(name):
    return f"Welcome to the {name} course !!!! " # http://127.0.0.1:5000/<course_name>

@app.route('/add/<int:a>/<int:b>')
def Add(a,b):
    return f"The sum of {a} and {b} is {a+b}" # http://127.0.0.1:5000/add/5/10

@app.route('/sub/<int:a>/<int:b>')
def Sub(a,b):
    return f"The difference of {a} and {b} is {a-b}" # http://127.0.0.1:5000/sub/10/5
app.run(debug=True)