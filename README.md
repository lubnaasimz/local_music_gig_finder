# Local Music Gig Finder API

A Flask REST API for managing music gigs, bands, venues, and reviews.

## API Endpoints

- `GET /api/shows` - Get all shows
- `GET /api/bands` - Get all bands  
- `GET /api/venues` - Get all venues
- `GET /api/users` - Get all users
- `GET /api/reviews` - Get all reviews
- `GET /api/musicians` - Get all musicians

All endpoints support full CRUD operations (GET, POST, PATCH, DELETE).

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

This API is configured for deployment on Render.com using the included `render.yaml` file.