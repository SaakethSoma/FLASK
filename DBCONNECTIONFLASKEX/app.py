from flask import Flask,render_template,request,redirect,url_for

#step-1: import connector
import mysql.connector

app = Flask(__name__)

#step-2: connection Flask/python app with mysql db
con=mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Saaketh1$$!!..',
    database = 'flaskdb')
#route for connection testing
@app.route('/')
def Home():
    return "Database is successfully connected !!!"

# route for  fetch data from database 
@app.route('/getstudents',methods=['GET'])
def Getstudents():
    # step-3 create cursor object 
    cursor=con.cursor()
    # send quaries to database by using cursor object
    cursor.execute('select * from students')
    # step-4 get data from resultset
    result=cursor.fetchall()
    cursor.close()
    

    return render_template('studentsdata.html',students=result)

# form for register the students
@app.route('/register',methods=['POST'])
def Register():
    sid=request.form['sid']
    sname=request.form['sname']
    sbranch=request.form['sbranch']
    smarks=request.form['smarks']
    sphno=request.form['sphno'] 

    cursor=con.cursor()
    cursor.execute(""" insert into students(sid,sname,sbranch,smarks,sphno) values(%s,%s,%s,%s,%s)""",(sid,sname,sbranch,smarks,sphno))

    con.commit()
    cursor.close()

    return redirect(url_for('GetStudents'))

# route for delete
@app.route('/delete/<int:sid>',methods=['GET'])
def Deletestudent(sid):
    cursor=con.cursor()
    cursor.execute("delete from students where sid=%s",(sid,))
    con.commit()
    cursor.close()
    return redirect(url_for("Getstudents"))

# route for edit 

@app.route('/edit/<int:sid>',methods=['GET'])
def Edit(sid):
    cursor=con.cursor()
    cursor.execute("select * from students where sid=%s",(sid,))
    result=cursor.fetchone()
    cursor.close()
    return render_template('edit.html',student=result)


# route for update

@app.route('/update',methods=['POST'])
def Update():
    sid=request.form['sid']
    sname=request.form['sname']
    sbranch=request.form['sbranch']
    smarks=request.form['smarks']
    sphno=request.form['sphno']

    cursor=con.cursor()
    cursor.execute("""update students set sname=%s,sbranch=%s,smarks=%s,sphno=%s
                   where sid=%s""",(sname,sbranch,smarks,sphno,sid))
    con.commit()
    cursor.close()
    return redirect(url_for("Getstudents"))


app.run(debug=True)