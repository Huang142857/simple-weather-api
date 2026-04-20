from rest_framework import viewsets
from .models import City, Weather
from .serializers import CitySerializer, WeatherSerializer

# ViewSet for City
# Provides CRUD operations for City
class CityViewSet(viewsets.ModelViewSet):
    # Query all city objects
    queryset = City.objects.all()
    # Use CitySerializer to validate and format data
    serializer_class = CitySerializer

# ViewSet for Weather
# Provides CRUD operations for Weather
class WeatherViewSet(viewsets.ModelViewSet):
    # Query all weather records
    queryset = Weather.objects.all()
    # Use WeatherSerializer to validate and format data
    serializer_class = WeatherSerializer