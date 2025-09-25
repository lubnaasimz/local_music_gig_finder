# backend/app.py

from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from config import db
from models import Band, Venue, Show, User, Review, ShowBand, Musician
from routes import shows_bp, reviews_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False

    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    app.register_blueprint(shows_bp)
    app.register_blueprint(reviews_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)