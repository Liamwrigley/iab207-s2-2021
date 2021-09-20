from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app=Flask(__name__)

    bootstrap = Bootstrap(app)
    app.secret_key="anything_at_all"
    
    #add Blueprints
    from . import views
    from . import destination
    from . import auth

    app.register_blueprint(views.mainbp)
    app.register_blueprint(destination.bp)
    app.register_blueprint(auth.bp)

    return app

