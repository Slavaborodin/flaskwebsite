import os


from flask import Flask
from os import path 
from flask_login import LoginManager
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST'] ='localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='viacheslav'
app.config['MYSQL_DATABASE_DB'] = 'Website'



def create_app():
    #initialising the app
    app = Flask(__name__)
    mysql.init_app(app)

    #secret key 
    app.config['SECRET_KEY']="helloworld"
  
    conn=mysql.connect()
    cursor=conn.cursor()



    #import the Blueprint from the views file
    from .views import views
    from .authentication import authentication
    
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(authentication,url_prefix="/")

   
    return app


