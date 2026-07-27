# Handles adding, viewing, and removing favorite restaurants.

from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required,current_user
from app import db
from app.models import Favorite
bp=Blueprint("favorites",__name__,url_prefix="/favorites")
@bp.route("/")
@login_required
def listing(): return render_template("favorites/list.html",favorites=Favorite.query.filter_by(user_id=current_user.id).all())
@bp.route("/add/<int:i>",methods=["POST"])
@login_required
def add(i):
    if not Favorite.query.filter_by(user_id=current_user.id,restaurant_id=i).first(): db.session.add(Favorite(user_id=current_user.id,restaurant_id=i)); db.session.commit()
    return redirect(url_for("restaurants.profile",i=i))
@bp.route("/remove/<int:i>",methods=["POST"])
@login_required
def remove(i):
    f=Favorite.query.filter_by(user_id=current_user.id,restaurant_id=i).first()
    if f: db.session.delete(f); db.session.commit()
    return redirect(url_for("favorites.listing"))
