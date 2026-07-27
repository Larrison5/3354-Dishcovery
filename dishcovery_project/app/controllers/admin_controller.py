# Handles administrator-only restaurant management pages.
# The admin_required decorator blocks regular customers from these routes.

from functools import wraps
from flask import Blueprint,render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from app.models import Restaurant
from app.repositories.restaurant_repository import RestaurantRepository as R
bp=Blueprint("admin",__name__,url_prefix="/admin")
def admin_required(fn):
    @wraps(fn)
    @login_required
    def w(*a,**k):
        if not current_user.is_admin():abort(403)
        return fn(*a,**k)
    return w
def fill(x,f):
    x.name=f.get("name","").strip(); x.cuisine=f.get("cuisine","").strip(); x.location=f.get("location","").strip(); x.address=f.get("address","").strip(); x.price_level=int(f.get("price_level","1")); x.rating=float(f.get("rating","0")); x.hours=f.get("hours","").strip(); x.menu=f.get("menu","").strip(); x.description=f.get("description","").strip(); x.dietary_options=f.get("dietary_options","").strip()
    if not all([x.name,x.cuisine,x.location,x.address,x.hours]): raise ValueError("Complete all required fields.")
    return x
@bp.route("/")
@admin_required
def dashboard():return render_template("admin/dashboard.html",restaurants=R.all())
@bp.route("/add",methods=["GET","POST"])
@admin_required
def add():
    if request.method=="POST":
        try:R.save(fill(Restaurant(),request.form)); return redirect(url_for("admin.dashboard"))
        except ValueError as e:flash(str(e),"error")
    return render_template("admin/form.html",restaurant=None,action="Add")
@bp.route("/<int:i>/edit",methods=["GET","POST"])
@admin_required
def edit(i):
    x=R.get(i)
    if not x:abort(404)
    if request.method=="POST":R.save(fill(x,request.form)); return redirect(url_for("admin.dashboard"))
    return render_template("admin/form.html",restaurant=x,action="Update")
@bp.route("/<int:i>/delete",methods=["POST"])
@admin_required
def delete(i):
    x=R.get(i)
    if not x:abort(404)
    R.delete(x); return redirect(url_for("admin.dashboard"))
