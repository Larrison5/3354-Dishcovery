# Handles register, login, and logout web requests.

from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,current_user
from app import db
from app.models import User
bp=Blueprint("auth",__name__,url_prefix="/auth")
@bp.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:return redirect(url_for("restaurants.home"))
    if request.method=="POST":
        n=request.form.get("name","").strip(); e=request.form.get("email","").lower().strip(); p=request.form.get("password","")
        if not n or not e or len(p)<6: flash("Enter all fields and use a 6 character password.","error")
        elif User.query.filter_by(email=e).first(): flash("Email already exists.","error")
        else:
            u=User(name=n,email=e,role="customer"); u.set_password(p); db.session.add(u); db.session.commit(); login_user(u); return redirect(url_for("preferences.manage"))
    return render_template("auth/register.html")
@bp.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        u=User.query.filter_by(email=request.form.get("email","").lower().strip()).first()
        if u and u.check_password(request.form.get("password","")): login_user(u); return redirect(url_for("restaurants.home"))
        flash("Invalid email or password.","error")
    return render_template("auth/login.html")
@bp.route("/logout")
def logout(): logout_user(); return redirect(url_for("restaurants.home"))
