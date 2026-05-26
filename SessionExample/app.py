from flask import Flask,session,redirect,render_template,url_for,request

from datetime import timedelta

app = Flask(__name__)

app.secret_key = "mysecretkey"

app.permanent_session_lifetime=timedelta(seconds=20)

# dummy database 
user = {'username':'raju','password':'raju123'}

@app.route('/',methods = ['GET','POST'])
def Login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['pwrd']

        if username==user['username'] and password==user['password']:
            session.permanent=True
            session['username'] = username  # {'username' : 'raju'}
            return redirect(url_for('Dashboard'))
        else:
            return "Invalid Username or Password <a href='/'>Login Again</a>"
        


    return render_template('login.html')

@app.route('/dashboard')
def Dashboard():
    if 'username' in session:
        return render_template('dashboard.html',user=session['username'])
    return redirect(url_for('Login'))

@app.route('/logout')
def Logout():
    session.pop('username')
    return redirect(url_for('Login'))

app.run(debug=True)