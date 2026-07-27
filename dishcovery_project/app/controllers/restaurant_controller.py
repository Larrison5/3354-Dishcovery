# Handles the public restaurant search and restaurant profile pages.

from flask import Blueprint,render_template,request,abort
from app.repositories.restaurant_repository import RestaurantRepository as R
bp=Blueprint("restaurants",__name__)
@bp.route("/")
def home():
    p=request.args.get("max_price",""); r=request.args.get("min_rating","")
    data=R.search(request.args.get("name",""),request.args.get("cuisine",""),request.args.get("location",""),int(p) if p else None,float(r) if r else None)
    return render_template("restaurants/home.html",restaurants=data)
@bp.route("/restaurants/<int:i>")
def profile(i):
    r=R.get(i)
    if not r: abort(404)
    return render_template("restaurants/profile.html",restaurant=r)
