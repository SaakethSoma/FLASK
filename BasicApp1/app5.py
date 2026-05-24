from flask import Flask, request

app=Flask(__name__)



@app.route('/register', methods=["GET","POST"])
def Register():
    if request.method=="POST":
        name=request.form["myname"]
        email=request.form["myemail"]
        password=request.form["mypassword"]
        return f"""
        <h1>Registration Successful</h1>
        <h1>Name is:{name}</h1>
        <h1>Email is:{email}</h1>
        <h1>password is:{password}</h1>
        """
    return f"""
<form action ="/register" method="POST">
    enter name:<input type="text" name="myname" id=required><br><br>
    enter email:<input type="email" name="myemail" id=required><br><br>
    enter password:<input type="password" name="mypassword" id=required><br><br>
    <input type="submit" value="Register">
    </form>
    """
    
app.run(debug=True)