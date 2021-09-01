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

    display_msg = '' 
    if request.method == 'POST' and 'username' in request.form and 'password1' in request.form and 'password2' in request.form and 'email' in request.form:
        username=request.form.get("username")
        email=request.form.get("email")
        pass1=request.form.get("password1")
        pass2=request.form.get("password2")

        conn=mysql.connect()
        cursor=conn.cursor()

        cursor.execute('SELECT * FROM User_Logins where user_username =%s' , (username,))

        get_useraccount=cursor.fetchone()

        if get_useraccount:
            display_msg='Sorry this account already exists!'
        elif not username or not email or not pass1 or not pass2:
            display_msg='Please fill out all components of the webform'
        else:
            cursor.execute ('INSERT INTO User_Logins VALUES (%s,%s,%s)', username,email,pass1)
            mysql.connection.comit()
            display_msg='You have now registered, Thank you!'

    elif request.method == 'POST':

        #return error if form is empty
        display_msg= 'The form has not been filled out, please fill out to proceed'

    return render_template("signup.htm",msg=display_msg)


@app.route("/Log-out")
def logout():

    session.pop('loggedin',None)
    session.pop('EMAIL',None)
    session.pop('PASSWORD',None)

    return redirect(url_for("login"))


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.htm")    


if __name__ == "__main__":
    app.run(debug=True)