import os


from flask import Flask,request,render_template,Blueprint,redirect
from os import path

from flask.globals import session 
from flask_login import LoginManager
from flaskext.mysql import MySQL
from flask.helpers import url_for


#import the Blueprint from the views file  
#from .views import views
#from .authentication import authentication

app = Flask(__name__)

mysql=MySQL()
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='viacheslav'
app.config['MYSQL_DATABASE_DB'] = 'Website'

#initialise db startup
mysql.init_app(app)

#authentication=Blueprint("authentication", __name__)

"""

def create_app():
    #initialising the app
    
   
    #secret key 
    app.config['SECRET_KEY']="helloworld"
    
    #connect to db
    conn=mysql.connect()
    cursor=conn.cursor()


    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(authentication,url_prefix="/")
    
    return app
"""

app = Flask(__name__)

# shows the home view
@app.route("/login",methods=['GET','POST'])
def login():

    #error message to tell user when something goes wrong 
    error_msg=''


    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        #get user credentials     
        email=request.form.get("email")
        password=request.form.get("password")

        conn=mysql.connect()
        cursor=conn.cursor()

        cursor.execute('SELECT * FROM User_Logins where user_username =%s and user_password =%s', (email,password,))

        account_status = cursor.fetchone()

        if account_status:
            session['loggedin'] = True
            session['id']= account_status['user_id']
            session['username'] = account_status['user_username']
            return 'Logged in Successfully'
        else:
            error_msg='Incorrect username/password'
            print(error_msg)


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