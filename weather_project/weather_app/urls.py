from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, WeatherViewSet, front_weather_data

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'weathers', WeatherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('front/data/', front_weather_data, name='front_weather_data'), 
]