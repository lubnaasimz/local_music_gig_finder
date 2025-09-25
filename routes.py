# backend/routes.py

from flask import Blueprint, jsonify, request
from config import db
from models import Show, Review, User, Band, Venue, Musician, ShowBand

# Blueprint definitions
shows_bp = Blueprint('shows', __name__, url_prefix='/api/shows')
bands_bp = Blueprint('bands', __name__, url_prefix='/api/bands')
venues_bp = Blueprint('venues', __name__, url_prefix='/api/venues')
users_bp = Blueprint('users', __name__, url_prefix='/api/users')
reviews_bp = Blueprint('reviews', __name__, url_prefix='/api/reviews')
musicians_bp = Blueprint('musicians', __name__, url_prefix='/api/musicians')

# SHOWS ENDPOINTS
@shows_bp.route('/', methods=['GET'])
def get_shows():
    shows = Show.query.all()
    return jsonify([show.to_dict() for show in shows]), 200

@shows_bp.route('/<int:show_id>', methods=['GET'])
def get_show(show_id):
    show = Show.query.get_or_404(show_id)
    return jsonify(show.to_dict()), 200

@shows_bp.route('/', methods=['POST'])
def create_show():
    data = request.get_json()
    show = Show(
        title=data.get('title'),
        date=data.get('date'),
        time=data.get('time'),
        ticket_price=data.get('ticket_price'),
        description=data.get('description'),
        venue_id=data.get('venue_id')
    )
    db.session.add(show)
    db.session.commit()
    return jsonify(show.to_dict()), 201

@shows_bp.route('/<int:show_id>', methods=['PATCH'])
def update_show(show_id):
    show = Show.query.get_or_404(show_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(show, key):
            setattr(show, key, value)
    
    db.session.commit()
    return jsonify(show.to_dict()), 200

@shows_bp.route('/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
    show = Show.query.get_or_404(show_id)
    db.session.delete(show)
    db.session.commit()
    return jsonify({'message': 'Show deleted successfully'}), 200

# BANDS ENDPOINTS
@bands_bp.route('/', methods=['GET'])
def get_bands():
    bands = Band.query.all()
    return jsonify([band.to_dict() for band in bands]), 200

@bands_bp.route('/<int:band_id>', methods=['GET'])
def get_band(band_id):
    band = Band.query.get_or_404(band_id)
    return jsonify(band.to_dict()), 200

@bands_bp.route('/', methods=['POST'])
def create_band():
    data = request.get_json()
    band = Band(
        name=data.get('name'),
        genre=data.get('genre'),
        description=data.get('description'),
        formed_year=data.get('formed_year')
    )
    db.session.add(band)
    db.session.commit()
    return jsonify(band.to_dict()), 201

@bands_bp.route('/<int:band_id>', methods=['PATCH'])
def update_band(band_id):
    band = Band.query.get_or_404(band_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(band, key):
            setattr(band, key, value)
    
    db.session.commit()
    return jsonify(band.to_dict()), 200

@bands_bp.route('/<int:band_id>', methods=['DELETE'])
def delete_band(band_id):
    band = Band.query.get_or_404(band_id)
    db.session.delete(band)
    db.session.commit()
    return jsonify({'message': 'Band deleted successfully'}), 200

# VENUES ENDPOINTS
@venues_bp.route('/', methods=['GET'])
def get_venues():
    venues = Venue.query.all()
    return jsonify([venue.to_dict() for venue in venues]), 200

@venues_bp.route('/<int:venue_id>', methods=['GET'])
def get_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    return jsonify(venue.to_dict()), 200

@venues_bp.route('/', methods=['POST'])
def create_venue():
    data = request.get_json()
    venue = Venue(
        name=data.get('name'),
        city=data.get('city'),
        address=data.get('address'),
        capacity=data.get('capacity'),
        phone=data.get('phone')
    )
    db.session.add(venue)
    db.session.commit()
    return jsonify(venue.to_dict()), 201

@venues_bp.route('/<int:venue_id>', methods=['PATCH'])
def update_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(venue, key):
            setattr(venue, key, value)
    
    db.session.commit()
    return jsonify(venue.to_dict()), 200

@venues_bp.route('/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    venue = Venue.query.get_or_404(venue_id)
    db.session.delete(venue)
    db.session.commit()
    return jsonify({'message': 'Venue deleted successfully'}), 200

# USERS ENDPOINTS
@users_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(
        username=data.get('username'),
        email=data.get('email'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@users_bp.route('/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    
    db.session.commit()
    return jsonify(user.to_dict()), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

# REVIEWS ENDPOINTS
@reviews_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

@reviews_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    return jsonify(review.to_dict()), 200

@reviews_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    review = Review(
        rating=data.get('rating'),
        comment=data.get('comment'),
        user_id=data.get('user_id'),
        show_id=data.get('show_id')
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201

@reviews_bp.route('/<int:review_id>', methods=['PATCH'])
def update_review(review_id):
    review = Review.query.get_or_404(review_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(review, key):
            setattr(review, key, value)
    
    db.session.commit()
    return jsonify(review.to_dict()), 200

@reviews_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully'}), 200

# MUSICIANS ENDPOINTS
@musicians_bp.route('/', methods=['GET'])
def get_musicians():
    musicians = Musician.query.all()
    return jsonify([musician.to_dict() for musician in musicians]), 200

@musicians_bp.route('/<int:musician_id>', methods=['GET'])
def get_musician(musician_id):
    musician = Musician.query.get_or_404(musician_id)
    return jsonify(musician.to_dict()), 200

@musicians_bp.route('/', methods=['POST'])
def create_musician():
    data = request.get_json()
    musician = Musician(
        name=data.get('name'),
        instrument=data.get('instrument'),
        bio=data.get('bio'),
        band_id=data.get('band_id')
    )
    db.session.add(musician)
    db.session.commit()
    return jsonify(musician.to_dict()), 201

@musicians_bp.route('/<int:musician_id>', methods=['PATCH'])
def update_musician(musician_id):
    musician = Musician.query.get_or_404(musician_id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(musician, key):
            setattr(musician, key, value)
    
    db.session.commit()
    return jsonify(musician.to_dict()), 200

@musicians_bp.route('/<int:musician_id>', methods=['DELETE'])
def delete_musician(musician_id):
    musician = Musician.query.get_or_404(musician_id)
    db.session.delete(musician)
    db.session.commit()
    return jsonify({'message': 'Musician deleted successfully'}), 200