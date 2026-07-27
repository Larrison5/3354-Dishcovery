# Handles restaurant database searches and changes.
# Controllers call this repository instead of writing SQL queries directly.

from app import db
from app.models import Restaurant
class RestaurantRepository:
    @staticmethod
    def all(): return Restaurant.query.order_by(Restaurant.rating.desc()).all()
    @staticmethod
    def get(i): return db.session.get(Restaurant,i)
    @staticmethod
    def search(name="",cuisine="",location="",max_price=None,min_rating=None):
        q=Restaurant.query
        if name:q=q.filter(Restaurant.name.ilike(f"%{name}%"))
        if cuisine:q=q.filter(Restaurant.cuisine.ilike(f"%{cuisine}%"))
        if location:q=q.filter(Restaurant.location.ilike(f"%{location}%"))
        if max_price is not None:q=q.filter(Restaurant.price_level<=max_price)
        if min_rating is not None:q=q.filter(Restaurant.rating>=min_rating)
        return q.order_by(Restaurant.rating.desc()).all()
    @staticmethod
    def save(x): db.session.add(x); db.session.commit(); return x
    @staticmethod
    def delete(x): db.session.delete(x); db.session.commit()
