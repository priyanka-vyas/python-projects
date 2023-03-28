# Create an API Project with following features:
# 1) Registration with email. Duplicacy check.
# 2) Login + JWT Token generation
# 3) Use Logger to track all actions
# 4) Create a frontend to upload a file, Save the file in a folder in the backend.
# 5) Create API to list down all the files in a folder and display it in frontend
# 6) Create a screen to input marks of 5 subjects of a student. Using API store data in database
# 7) Create a screen to display the avg marks and a pie chart of subjects the data should fetched using APIs
# 8) After logout, pressing browser back button should not show the data
from flask import *
from distutils.log import debug
from fileinput import filename
import re
import os
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = "secret key"
app.config["MySQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password1234"
app.config["MYSQL_DB"] = "Flask "
mysql = MYSQL(app)


@app.route('/')
def main():
    return render_template("upload.html")


@app.route('/success', method=["POST"])
def success():
    # upload file
    if request.method == 'POST':
        f = request.files('file')
        f.save(f.filename)
        return render_template("Acknowledgement.html", name=f.filename)


# register with email
@app.route("/register", method=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST" and "email" in request.form and 'password' in request.form:
        email = request.form["email"]
        password = request.form["password"]
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from accounts where email=%s",(email,))
        account=cursor.fetchone()
        if account:
            msg = "Account already exist!"
        elif not re.match(r'[^@+@[^@]+\.[^@]+', email):
            msg = "Invalid email address!"
        else:
            cursor.execute("Insert into accounts values(NULL, %s, %s) ",(email,password))
            mysql.connection.commit()
            msg="Successfully registered"
    elif request.method == "POST":
        msg = "Please fill out the form!"

        return render_template("register.html", msg=msg)


# login
@app.route("/login", method=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST" and "email" in request.form and 'password' in request.form:
        email = request.form["email"]
        password = request.form["password"]
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("select * from accounts where email=%s and password=%s",(email,password))
        account=cursor.fetchone()
        if account:
            session["email"] == account["email"]
            session["password"] == account["password"]
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect Password"
    return render_template("login.html", msg=msg)
#create a drop down and display all files
path="C:\Users\info\PycharmProjects\pythonProject\Flask_interview"
@app.route("/list_of_files",method=["POST","GET"])
def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            return (os.listdir(path))
    files=[]
    for file in  get_files(path):
        files.append(file)
        print(files)
        return render_template("home.html",files=get_files(path))

@app.route("/data",method=["GET", "POST"]):
def student_details():
    msg = ""
    for i in range(0,5):
        if request.method == "POST" and "subject" in request.form and 'marks' in request.form:
            subject = request.form["subject"]
            mark = request.form["mark"]
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("Insert into accounts values(NULL, %s, %s) ", (subject, mark))
            mysql.connection.commit()
            msg = "Successfully inserted"
    return msg
@app.route("/avg_marks",method=[ "POST"]):
def avg_marks():
    msg = ""
    marks=0
    for i in range(0,5):
        if request.method == "POST" :
            subject = request.form["subject"]
            mark = request.form["mark"]
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("Insert into accounts values(NULL, %s, %s) ", (subject, mark))
            account = cursor.fetchone()
            if account:
                marks += account["mark"]
            msg = marks
    return marks


# logout
@app.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('password', None)
    return redirect(url_for('login'))


if __name__=="main":
    app.run(debug==True)

