import os
import secrets


from flask import Flask,request,render_template,Blueprint,redirect,session
from os import path

from flask_login import LoginManager
from flaskext.mysql import MySQL
from flask.helpers import url_for

app = Flask(__name__)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='pass'
app.config['MYSQL_DATABASE_DB'] = 'Website'

#initialise db startup
mysql.init_app(app)

app = Flask(__name__)
#secret key 
app.config['SECRET_KEY']=secrets.token_urlsafe(16)

print(secrets.token_urlsafe(16))

# shows the home view
@app.route("/login",methods=['GET','POST'])
def login():

    #error message to tell user when something goes wrong 
    error_msg=''

    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        #get user credentials     
        email=request.form['email'].strip()
        password=request.form['password'].strip()

        conn=mysql.connect()
        cursor=conn.cursor()

        cursor.execute('SELECT * FROM User_Logins where user_email =%s and user_password =%s', (email,password,))

        account_status = cursor.fetchone()

        if  account_status:
            session['loggedin'] = True
            session["EMAIL"] = account_status[1] 
            print(session)
            session["PASSWORD"] = account_status[2]
            print(session)
            return 'Logged in Successfully'
            # return redirect(url_for("profile"))
           
        else:
            error_msg='Incorrect username/password'
            print(error_msg)
            return redirect(url_for("login"))

    return render_template("login.htm",msg=error_msg)

@app.route("/Sign-up", methods=['GET','POST'])
def signup():
    username=request.form.get("username")
    email=request.form.get("email")
    pass1=request.form.get("password1")
    pass2=request.form.get("password2")

    return render_template("signup.htm")


@app.route("/Log-out")
def logout():
    return redirect(url_for("home.htm"))


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.htm")    


if __name__ == "__main__":
    app.run(debug=True)