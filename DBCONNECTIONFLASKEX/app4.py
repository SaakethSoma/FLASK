from flask import Flask,session

app = Flask(__name__)
app.secret_key ="abcxyz123"

@app.route('/',methods=['GET'])
def Login():
    session['username']= 'raju'  # {"username":"raju"}
    return "Logged In"

@app.route('/dashboard',methods=['GET'])
def Dashboard():
    if 'username' in session:
        return f"Welcome {session['username']}"
    return "Not available"

@app.route('/logout',methods=['GET'])
def Logout():
    session.pop('username')
    return "Logged Out"

app.run(debug=True)