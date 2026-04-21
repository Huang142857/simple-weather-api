# Weather API - XJCO3011 Coursework 1
A fully functional RESTful API for weather data management, built with Django & Django REST Framework.

## Student Information
- Name: Siyuan Huang
- Student ID: 2022116028
- Module: XJCO3011 Web Services and Web Data
- GitHub: https://github.com/Huang142857/simple-weather-api.git

---

## Project Features
- Complete CRUD operations for City and Weather entities
- One-to-many relational database design
- Token-based authentication for secure API access
- Pagination (5 items per page)
- API rate throttling (30 requests/minute for authenticated users)
- Automatic API request logging
- Swagger UI API documentation
- Frontend dashboard for data visualization
- Standard HTTP status codes and error responses
- Data validation and secure ORM-based database access

---

## Technology Stack
- Backend: Django 5 + Django REST Framework
- Database: SQLite
- API Documentation: drf-yasg (Swagger UI)
- Frontend: HTML, CSS, Vanilla JavaScript
- Authentication: Token Authentication
- Security: Throttling, Input Validation, Logging

---

## Installation & Local Setup
1. Clone the repository
git clone https://github.com/Huang142857/simple-weather-api.git
cd weather_project

2. Install dependencies
pip install -r requirements.txt

3. Run migrations
python manage.py makemigrations
python manage.py migrate

4. Create a superuser
python manage.py createsuperuser

5. Run the server
python manage.py runserver

---

## API Authentication
All API endpoints require token authentication.

### Get Your Token
Run in Django shell:
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
user = User.objects.first()
token = Token.objects.create(user=user)
print(token.key)

### Use Token in Requests
Header:
Authorization: Token YOUR_TOKEN_HERE

---

## API Endpoints
- GET /api/cities/ – List all cities (paginated)
- POST /api/cities/ – Create a city
- GET /api/weathers/ – List weather records (paginated)
- POST /api/weathers/ – Create a weather record
- GET /api/front/data/ – Frontend data endpoint
- GET /swagger/ – API documentation (Swagger UI)
- /admin/ – Django admin panel

---

## Documentation
- API Documentation: /swagger/
- PDF Documentation: docs/API_DOCUMENTATION.pdf
- Technical Report: docs/Technical_Report.pdf

---

## Logs
All API requests are logged to:
api_requests.log

---

## Deployment
This project can be deployed to:
- PythonAnywhere
- Local server
- Any WSGI-compatible platform

---

## Acknowledgements
This project was developed for XJCO3011 Web Services & Web Data coursework at the University of Leeds.
