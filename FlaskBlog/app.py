import os


from flask import Flask,request,render_template,Blueprint,redirect
from os import path 
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
    email=request.form.get("email")
    password=request.form.get("password")
    
    return render_template("login.htm")

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