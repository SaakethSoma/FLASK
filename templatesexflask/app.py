from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def Home():
    return "<h3>Welcome to Home Page</h3>"

@app.route('/home1')
def Home1():
    return render_template('home.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def Contact():
    name="harini"
    phno="9089765478"
    return render_template('contact.html',result=name,phno=phno)

@app.route('/info')
def Info():
    names=['rani','ramu','kalyani','madhulatha','harini']
    return render_template('info.html',result=names)

app.run(debug=True)