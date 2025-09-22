# backend/models.py

from config import db
from sqlalchemy.ext.associationproxy import association_proxy

class ShowBand(db.Model):
    __tablename__ = 'show_bands'
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'))
    set_order = db.Column(db.Integer)

    show = db.relationship('Show', back_populates='show_bands')
    band = db.relationship('Band', back_populates='show_bands')

class Band(db.Model):
    __tablename__ = 'bands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    
    musicians = db.relationship('Musician', backref='band', cascade='all, delete-orphan')
    show_bands = db.relationship('ShowBand', back_populates='band', cascade='all, delete-orphan')
    shows = association_proxy('show_bands', 'show')

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String)
    
    shows = db.relationship('Show', backref='venue', cascade='all, delete-orphan')

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    time = db.Column(db.String)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    
    reviews = db.relationship('Review', backref='show', cascade='all, delete-orphan')
    show_bands = db.relationship('ShowBand', back_populates='show', cascade='all, delete-orphan')
    bands = association_proxy('show_bands', 'band')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

    reviews = db.relationship('Review', backref='user', cascade='all, delete-orphan')

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))

class Musician(db.Model):
    __tablename__ = 'musicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    instrument = db.Column(db.String)
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'))