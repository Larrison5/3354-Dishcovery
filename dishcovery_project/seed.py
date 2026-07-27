# Creates a fresh database with sample users and restaurants.
# Run this file when setting up the project for the first time.

from app import create_app,db
from app.models import User,Restaurant
app=create_app()
# Flask needs an application context before database commands can run.
with app.app_context():
 db.drop_all();db.create_all()
 a=User(name="Dishcovery Admin",email="admin@dishcovery.com",role="admin");a.set_password("admin123")
 c=User(name="Demo Customer",email="customer@dishcovery.com",role="customer");c.set_password("customer123")
 db.session.add_all([a,c])
 data=[("Seoul Garden","Korean","Dallas","101 Main St",2,4.6,"11 AM-10 PM","BBQ, bibimbap","Korean barbecue","Vegetarian options"),("Tokyo Table","Japanese","Richardson","220 Belt Line",2,4.4,"12 PM-9 PM","Sushi, ramen","Japanese comfort food","Gluten-free options"),("Taco Plaza","Mexican","Plano","450 Parker Rd",1,4.2,"10 AM-11 PM","Tacos, burritos","Mexican street food","Vegetarian options"),("Cedar Grill","Mediterranean","Irving","88 Las Colinas",2,4.5,"11 AM-10 PM","Gyro, shawarma","Mediterranean favorites","Halal, vegetarian options")]
 for x in data: db.session.add(Restaurant(name=x[0],cuisine=x[1],location=x[2],address=x[3],price_level=x[4],rating=x[5],hours=x[6],menu=x[7],description=x[8],dietary_options=x[9]))
 db.session.commit();print("Seeded. Admin admin@dishcovery.com/admin123; Customer customer@dishcovery.com/customer123")
