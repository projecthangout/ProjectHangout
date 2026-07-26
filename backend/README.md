# Project Hangout - Backend

This is the backend API and WebSocket server for Project Hangout, built with Django and Django Channels.

## 🚀 Tech Stack

- **Framework**: [Django](https://www.djangoproject.com/) (v6.0+)
- **API**: [Django REST Framework](https://www.django-rest-framework.org/)
- **WebSockets**: [Django Channels](https://channels.readthedocs.io/en/latest/) & [Daphne](https://github.com/django/daphne)
- **Media Storage**: [Cloudinary](https://cloudinary.com/)
- **CORS Handling**: `django-cors-headers`

## 📦 Getting Started

### Prerequisites

Make sure you have Python (v3.10+ recommended) and `pip` installed.

### Installation

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables

Create a `.env` file in the `backend` directory with the necessary environment variables. These might include your Django `SECRET_KEY`, `DEBUG` flag, database credentials, and Cloudinary API keys. 

*Note: Ensure your `.env` file is never committed to version control. It is already included in `.gitignore`.*

### Database Setup

Run the migrations to set up your local database schema (defaults to SQLite):
```bash
python manage.py migrate
```

### Running the Server

Start the ASGI development server (which handles both standard HTTP requests and WebSockets):
```bash
python manage.py runserver
```

## 📁 Apps Structure

- `core/` - Main Django settings and ASGI/WSGI configuration.
- `users/` - User authentication and management functionality.
- `meetings/` - Logic for handling video/audio meetings and signaling.
