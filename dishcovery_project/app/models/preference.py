# Stores a customer's dining preferences.
# Each user has one preference record that can be updated later.

from app import db
class Preference(db.Model):
    id=db.Column(db.Integer,primary_key=True); cuisine=db.Column(db.String(80)); max_price_level=db.Column(db.Integer); location=db.Column(db.String(120)); minimum_rating=db.Column(db.Float); dietary_options=db.Column(db.String(200)); user_id=db.Column(db.Integer,db.ForeignKey("user.id"),unique=True,nullable=False); user=db.relationship("User",back_populates="preference")
    def update_from_form(self,f):
        self.cuisine=f.get("cuisine","").strip(); self.location=f.get("location","").strip(); self.dietary_options=f.get("dietary_options","").strip(); p=f.get("max_price_level","").strip(); r=f.get("minimum_rating","").strip(); self.max_price_level=int(p) if p else None; self.minimum_rating=float(r) if r else None
