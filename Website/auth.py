from flask import Blueprint, render_template, request, redirect

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ['GET','POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/signup", methods = ['GET','POST'])
def sign_up():
    email = request.form.get("email")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return "Logout"


