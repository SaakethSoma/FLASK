from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def Home():
    image='agra.jpg'
    return render_template('home.html',result=image)


@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def Contact():
    return render_template('contact.html')


app.run(debug=True)