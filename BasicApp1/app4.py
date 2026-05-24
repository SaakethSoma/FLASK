from flask import Flask
app = Flask(__name__)

# example for string url-convertor
@app.route('/<string:name>')
def Home(name):
    print("datatype is:", type(name))
    return f"value is :{name}"

# example for int url-convertor
@app.route('/square/<int:num>')
def Square(num):
    print("datatype is:", type(num))
    return f"square of {num} is :{num**2}"

#example for float url-convertor
@app.route('/half/<float:price>')
def Half(price):
    print("datatype is:",type(price))
    return f"half of {price} is :{price/2}"

#example for path url-convertor
@app.route('/file/<path:filepath>')
def Show_file(filepath):
    print("datatype is :",type(filepath))
    return f"file path is :{filepath}"

#example for uuid url-convertor
@app.route('/item/<uuid:id>')
def Item(id):
    print("datatype is :",type(id))
    return f"UUID object is :{id}"

app.run(debug=True)