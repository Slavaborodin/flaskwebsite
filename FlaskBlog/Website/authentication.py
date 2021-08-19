from flask import Blueprint, render_template, request,redirect
from flask.helpers import url_for

authentication=Blueprint("authentication", __name__)


# shows the home view
@authentication.route("/login",methods=['GET','POST'])
def login():
    email=request.form.get("email")
    password=request.form.get("password")
    
    return render_template("login.htm")

@authentication.route("/Sign-up", methods=['GET','POST'])
def signup():
    username=request.form.get("username")
    email=request.form.get("email")
    pass1=request.form.get("password1")
    pass2=request.form.get("password2")

    return render_template("signup.htm")


@authentication.route("/Log-out")
def logout():
    print ("Logging out")
    return redirect(url_for("views.home"))

