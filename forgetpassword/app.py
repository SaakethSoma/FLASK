from flask import Flask, render_template, request, redirect, flash, session
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "saakethsoma@gmail.com"
app.config['MAIL_PASSWORD'] = "xsld jlat hvgw esaw"

mail = Mail(app)

# Token Serializer
s = URLSafeTimedSerializer(app.secret_key)

# Dummy database
users = {"saakethsoma@gmail.com": {"password": "saaketh1234"}}

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if email in users and users[email]["password"] == password:
        session['email'] = email
        return redirect("/dashboard")
    else:
        flash("Invalid Login!")
        return redirect("/")

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template("dashboard.html", user=session['email'])
    return redirect('/')

@app.route('/forgot_password')
def forgot_password():
    return render_template("forgot_password.html")

@app.route('/send_reset_link', methods=['POST'])
def send_reset_link():
    email = request.form['email']
    
    if email not in users:
        flash("Email not registered!")
        return redirect('/forgot_password')

    token = s.dumps(email, salt='password-reset-salt')
    link = f"http://localhost:5000/reset_password/{token}"

    msg = Message("Password Reset Request", sender="saakethsoma@gmail.com", recipients=[email])
    msg.body = f"Click the link to reset your password: {link}"
    mail.send(msg)

    flash("Reset link sent to your email!")
    return redirect('/')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=100)  # valid for 5 minutes
    except SignatureExpired:
        return "Link expired! Try again."

    if request.method == 'POST':
        new_password = request.form['password']
        users[email]["password"] = new_password
        flash("Password reset successful! Please login.")
        return redirect('/')

    return render_template("reset_password.html")
    
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)