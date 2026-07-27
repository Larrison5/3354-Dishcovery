from app import create_app,db
from app.models import User,Restaurant,Preference
from app.services.matching_service import MatchingService
def test_matching():
 app=create_app({"TESTING":True,"SQLALCHEMY_DATABASE_URI":"sqlite:///:memory:"})
 with app.app_context():
  db.create_all();u=User(name="T",email="t@x.com",role="customer");u.set_password("secret1");db.session.add(u);db.session.flush();r=Restaurant(name="K",cuisine="Korean",location="Dallas",address="A",price_level=2,rating=4.8,hours="11-9");db.session.add(r);db.session.commit();p=Preference(cuisine="Korean",location="Dallas",max_price_level=2,minimum_rating=4,user_id=u.id);x=MatchingService.score(r,p);assert x.score>80
