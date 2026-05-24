from flask import Flask,jsonify,request
app=Flask(__name__)

students=[
    {"id":101,"name":"raju","branch":"CSE","age":22},
    {"id":102,"name":"ram","branch":"IT","age":25},
]

# 101 ---> CSE ----> CIVIL

# update route
@app.route('/studentupdate/<int:sid>',methods =['PUT'])  # http://127.0.0.1:5000/studentupdate/101
def Studentupdate(sid):
    global students
    data = request.get_json()

    for stu in students:
        if stu["id"]==sid:
            stu["branch"]=data["branch"]
            # stu["age"]=data["age"]
            return jsonify({"message":f"student id {sid} is updated successfully","updated data is":students}),200
    return jsonify({"message":f"student id {sid} is not found"}),404

# delete route
@app.route('/studentsdelete/<int:sid>',methods=['DELETE'])   # http://127.0.0.1:5000/studentsdelete/101
def Studentsdelete(sid):
    global students
    for stu in students:
        if stu['id']==sid:
            students.remove(stu)
            return jsonify({'message': f'student id {sid} deleted successfully','remaining data is':students}),200
    return jsonify({'message': f'student id {sid} not found'}),404  
app.run(debug=True)