# Handles saving dining preferences and showing restaurant matches.

from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,current_user
from app import db
from app.models import Preference
from app.services.matching_service import MatchingService
bp=Blueprint("preferences",__name__,url_prefix="/preferences")
@bp.route("/",methods=["GET","POST"])
@login_required
def manage():
    p=Preference.query.filter_by(user_id=current_user.id).first()
    if request.method=="POST":
        p=p or Preference(user_id=current_user.id)
        try: p.update_from_form(request.form); db.session.add(p); db.session.commit(); return redirect(url_for("preferences.matches"))
        except ValueError: flash("Enter valid numbers.","error")
    return render_template("preferences/manage.html",preference=p)
@bp.route("/matches")
@login_required
def matches():
    p=Preference.query.filter_by(user_id=current_user.id).first()
    if not p:return redirect(url_for("preferences.manage"))
    return render_template("preferences/matches.html",results=MatchingService.find_matches(p))
