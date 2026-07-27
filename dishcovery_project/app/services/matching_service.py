# Calculates how well each restaurant matches a customer's preferences.
# Restaurants with higher scores appear first in the recommendation list.

from dataclasses import dataclass
from app.repositories.restaurant_repository import RestaurantRepository
@dataclass
class MatchResult: restaurant:object; score:float; reasons:list
class MatchingService:
    @staticmethod
    def find_matches(p):
        out=[MatchingService.score(r,p) for r in RestaurantRepository.all()]; out.sort(key=lambda x:(x.score,x.restaurant.rating),reverse=True); return out
    @staticmethod
    def score(r,p):
        s=0; why=[]
        if p.cuisine and p.cuisine.lower() in r.cuisine.lower(): s+=40; why.append("Matches preferred cuisine")
        if p.location and p.location.lower() in r.location.lower(): s+=20; why.append("Matches preferred location")
        if p.max_price_level is not None and r.price_level<=p.max_price_level: s+=15; why.append("Within price range")
        if p.minimum_rating is not None and r.rating>=p.minimum_rating: s+=15; why.append("Meets minimum rating")
        if p.dietary_options and any(x.strip().lower() in (r.dietary_options or '').lower() for x in p.dietary_options.split(',')): s+=10; why.append("Supports dietary preferences")
        s+=min(5,r.rating); return MatchResult(r,round(s,1),why)
