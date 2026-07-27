# Sets up Flask, the database, login management, and all controllers.
# The create_app function makes the project easier to test and organize.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db=SQLAlchemy(); login_manager=LoginManager(); login_manager.login_view="auth.login"
def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dishcovery-dev",SQLALCHEMY_DATABASE_URI="sqlite:///dishcovery.db",SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if test_config: app.config.update(test_config)
    db.init_app(app); login_manager.init_app(app)
    from app.controllers.auth_controller import bp as auth
    from app.controllers.restaurant_controller import bp as restaurants
    from app.controllers.preference_controller import bp as preferences
    from app.controllers.favorite_controller import bp as favorites
    from app.controllers.admin_controller import bp as admin
    for b in [auth,restaurants,preferences,favorites,admin]: app.register_blueprint(b)
    with app.app_context(): db.create_all()
    return app
