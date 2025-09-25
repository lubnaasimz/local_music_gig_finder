# backend/models.py

from config import db
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

class ShowBand(db.Model):
    __tablename__ = 'show_bands'
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'))
    set_order = db.Column(db.Integer)

    show = db.relationship('Show', back_populates='show_bands')
    band = db.relationship('Band', back_populates='show_bands')

    def to_dict(self):
        return {
            'id': self.id,
            'show_id': self.show_id,
            'band_id': self.band_id,
            'set_order': self.set_order
        }

class Band(db.Model):
    __tablename__ = 'bands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String)
    description = db.Column(db.Text)
    formed_year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    musicians = db.relationship('Musician', backref='band', cascade='all, delete-orphan')
    show_bands = db.relationship('ShowBand', back_populates='band', cascade='all, delete-orphan')
    shows = association_proxy('show_bands', 'show')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'description': self.description,
            'formed_year': self.formed_year,
            'musicians': [m.to_dict() for m in self.musicians],
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String)
    address = db.Column(db.String)
    capacity = db.Column(db.Integer)
    phone = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    shows = db.relationship('Show', backref='venue', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'address': self.address,
            'capacity': self.capacity,
            'phone': self.phone,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    date = db.Column(db.String)
    time = db.Column(db.String)
    ticket_price = db.Column(db.Float)
    description = db.Column(db.Text)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    reviews = db.relationship('Review', backref='show', cascade='all, delete-orphan')
    show_bands = db.relationship('ShowBand', back_populates='show', cascade='all, delete-orphan')
    bands = association_proxy('show_bands', 'band')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'ticket_price': self.ticket_price,
            'description': self.description,
            'venue': self.venue.to_dict() if self.venue else None,
            'bands': [sb.band.to_dict() for sb in self.show_bands],
            'reviews': [r.to_dict() for r in self.reviews],
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship('Review', backref='user', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'comment': self.comment,
            'user': self.user.to_dict() if self.user else None,
            'show_id': self.show_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Musician(db.Model):
    __tablename__ = 'musicians'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    instrument = db.Column(db.String)
    bio = db.Column(db.Text)
    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'instrument': self.instrument,
            'bio': self.bio,
            'band_id': self.band_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }