# backend/routes.py

from flask import Blueprint, jsonify, request
from config import db
from models import Show, Review, User

shows_bp = Blueprint('shows', __name__, url_prefix='/shows')
reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@shows_bp.route('/')
def get_shows():
    shows = Show.query.all()
    return jsonify([{
        'id': show.id,
        'date': show.date,
        'time': show.time,
        'venue_name': show.venue.name,
        'bands': [band.name for band in show.bands]
    } for show in shows]), 200

@shows_bp.route('/<int:show_id>')
def get_show(show_id):
    show = Show.query.get(show_id)
    if not show:
        return jsonify({'error': 'Show not found'}), 404

    reviews = [{'id': r.id, 'rating': r.rating, 'comment': r.comment, 'username': r.user.username} for r in show.reviews]
    
    return jsonify({
        'id': show.id,
        'date': show.date,
        'time': show.time,
        'venue_name': show.venue.name,
        'bands': [band.name for band in show.bands],
        'reviews': reviews
    }), 200

@reviews_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    new_review = Review(
        rating=data.get('rating'),
        comment=data.get('comment'),
        user_id=data.get('user_id'),
        show_id=data.get('show_id')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review created successfully!'}), 201

@reviews_bp.route('/<int:review_id>', methods=['PATCH'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    
    data = request.get_json()
    for key, value in data.items():
        setattr(review, key, value)
    
    db.session.commit()
    return jsonify({'message': 'Review updated successfully!'}), 200

@reviews_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return jsonify({'message': 'Review deleted successfully!'}), 200