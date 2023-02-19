from flask import Blueprint, render_template, request, redirect, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged In!", category="success")
                login_user(user, remember=True)
                return render_template("home.html")
            else:
                flash("Incorrect Password",category="error")
        else:
            flash("Email has not been registered",category="error")        

    
    
    return render_template("login.html")

@auth.route("/signup", methods = ['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash('Email is already in use', category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 8:
            flash("Password must be at least 8 characters long", category='error')
        else:
            new_user = User(email = email, password = generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            flash("User Created!")
            return render_template("home.html")


    
    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("login.html")


