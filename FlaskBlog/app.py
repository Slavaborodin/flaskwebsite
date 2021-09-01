import os
import secrets


from flask import Flask,request,render_template,Blueprint,redirect,session,flash
from os import error, path

from flask_login import LoginManager
from flaskext.mysql import MySQL
from flask.helpers import flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash

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
            session['id'] = account_status[0]
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
            flash('Sorry this account already exists!',error=error)
        elif not username or not email or not pass1 or not pass2:
            flash('Please fill out all components of the webform',error=error)
        elif pass1 != pass2:
            flash('Passwords don\'t match!',category=error)
        elif len(username)<2:
            flash('Username is too short', error=error)
        elif len(pass1) < 6:
            flash('Password is too short',error=error)
        elif len(email) < 3: 
            flash ('Email Address is Invalid', error=error)    
        else:
            cursor.execute ('INSERT INTO User_Logins VALUES (%s,%s,%s)', username,email,generate_password_hash(pass1,method='sha256'))
            mysql.connection.comit()
            flash('User has been created!')

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


@app.route("/loggedin/home")
def loggedinhome():

    if 'loggedin' in session:
        # if the user is logged return their session 
        return render_template('home.htm',username=session['username'])

    #otherwise prompt the user to log in 
    return redirect(url_for('login'))

@app.route("/loggedin/useraccount")
def useraccount():

    if 'loggedin' in session:
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM User_Logins where user_id =%s' , (session['user_id'],))
        
        get_useraccount=cursor.fetchone()
        return render_template('profile.htm',get_useraccount=get_useraccount)

    return redirect(url_for('login'))    

if __name__ == "__main__":
    app.run(debug=True)