#step1 : import flask class from flask
from flask import Flask
#step2 : create instance of flask
app = Flask(__name__)   
#step3 : define route
@app.route('/')
def home():
    return "Welcome to Home"
@app.route('/about')
def about():
    return "Welcome to About"
@app.route('/contact')
def contact():
    return "Welcome to Contact"
#step4 : run the application
app.run()