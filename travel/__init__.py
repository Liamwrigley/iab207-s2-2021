from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app=Flask(__name__)

    bootstrap = Bootstrap(app)
    app.secret_key="anything_at_all"
    
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travelDB.sqlite'

    db.init_app(app)

    
    #add Blueprints
    from . import views
    from . import destination
    from . import auth

    app.register_blueprint(views.mainbp)
    app.register_blueprint(destination.bp)
    app.register_blueprint(auth.bp)

    return app

