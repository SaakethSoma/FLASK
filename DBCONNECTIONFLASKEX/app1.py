from flask import Flask,request

app=Flask(__name__)


@app.route('/')
def Home():
    return "Hello World"

@app.route('/getdata')   # http://127.0.0.1:5000/getdata?name=harini&age=34
def Getdata():
    nname=request.args.get('name',default="ramya")
    nage=request.args.get('age', type=int)

    print("datatype of name and age is",type(nname),type(nage))
    return f"nname is :{nname} and age is: {nage}"


@app.route('/getcolors')  # http://127.0.0.1:5000/getcolors?color=red&color=yellow&color=pink
def Getcolors():
    colors=request.args.getlist('color')
    return f"my colors are {colors}"



app.run(debug=True)