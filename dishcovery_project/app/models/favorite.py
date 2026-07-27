# Connects a user to a restaurant they saved as a favorite.
# The unique constraint prevents the same restaurant from being saved twice.

from datetime import datetime,timezone
from app import db
class Favorite(db.Model):
    __table_args__=(db.UniqueConstraint("user_id","restaurant_id"),)
    id=db.Column(db.Integer,primary_key=True); date_saved=db.Column(db.DateTime,default=lambda:datetime.now(timezone.utc),nullable=False); user_id=db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False); restaurant_id=db.Column(db.Integer,db.ForeignKey("restaurant.id"),nullable=False); user=db.relationship("User",back_populates="favorites"); restaurant=db.relationship("Restaurant",back_populates="favorites")
