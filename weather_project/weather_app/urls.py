from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, WeatherViewSet

# Router object to auto-generate API URLs
router = DefaultRouter()

# Register City routes
router.register(r'cities', CityViewSet)

# Register Weather routes
router.register(r'weathers', WeatherViewSet)

# Include all router-generated URLs
urlpatterns = [
    path('', include(router.urls)),
]