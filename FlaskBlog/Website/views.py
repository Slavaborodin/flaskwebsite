from flask import Blueprint,render_template

views=Blueprint("views", __name__)


# shows the home view by default
@views.route("/")
@views.route("/home")
def home():
    return render_template("home.htm")