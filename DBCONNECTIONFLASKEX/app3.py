from flask import Flask,make_response

app = Flask(__name__)
@app.route('/set_cookie')

def set_cookie():
    res=make_response("cookie set")
    res.set_cookie("username","saaketh")
    return res

@app.route('/get_cookie')
def get_cookie():
    from flask import request
    user = request.cookie.get("username")
    return f"cookie value={user}"

app.run(debug=True)