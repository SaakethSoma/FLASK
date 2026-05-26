from flask import Flask,render_template,request,redirect,url_for

import mysql.connector

app=Flask(__name__)

con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Saaketh1$$!!..',
    database='student_db'
)

@app.route('/')
def Home():
    return render_template('register.html')



@app.route('/api/students',methods=['GET'])
def Getstudents():
    cursor=con.cursor()
    cursor.execute('select * from students')
    result=cursor.fetchall()
    return render_template('studentsdata.html',students=result)


@app.route('/api/students',methods=['POST'])
def Register():
    id=request.form['id']
    name=request.form['name']
    email=request.form['email']
    course=request.form['course']
    phone=request.form['phone']

    cursor=con.cursor()
    cursor.execute("""insert into students(id,name,email,course,phone) values(%s,%s,%s,%s,%s)""",(id,name,email,course,phone))
    con.commit()

    return redirect(url_for("Getstudents"))



@app.route('/delete/<int:id>',methods=['GET'])
def Deletestudent(id):
    cursor=con.cursor()
    cursor.execute("delete from students where id=%s",(id,))
    con.commit()
    # cursor.close()
    return redirect(url_for("Getstudents"))


@app.route('/edit/<int:id>',methods=['GET'])
def Edit(id):
    cursor=con.cursor()
    cursor.execute("select * from students where id=%s",(id,))
    result=cursor.fetchone()
    cursor.close()
    return render_template('edit.html',student=result)
    

@app.route('/api/students/<int:id>',methods=['POST'])
def Update(id):
    id=request.form['id']
    name=request.form['name']
    email=request.form['email']
    course=request.form['course']
    phone=request.form['phone']


    cursor=con.cursor()
    cursor.execute("""update students set name=%s,email=%s,course=%s,phone=%s where id=%s""",(name,email,course,phone,id))
    con.commit()
    return redirect(url_for("Getstudents"))
app.run(debug=True)