# Represents a restaurant stored in the Dishcovery database.
# The fields match the information shown on restaurant profile pages.

from app import db
class Restaurant(db.Model):
    id=db.Column(db.Integer,primary_key=True); name=db.Column(db.String(150),nullable=False,index=True); cuisine=db.Column(db.String(80),nullable=False,index=True); location=db.Column(db.String(120),nullable=False,index=True); address=db.Column(db.String(200),nullable=False); price_level=db.Column(db.Integer,nullable=False); rating=db.Column(db.Float,nullable=False,default=0); hours=db.Column(db.String(150),nullable=False); menu=db.Column(db.Text); description=db.Column(db.Text); dietary_options=db.Column(db.String(200))
    favorites=db.relationship("Favorite",back_populates="restaurant",cascade="all, delete-orphan")
