from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import City, Weather
from .serializers import CitySerializer, WeatherSerializer

# -----------------------------------------------------------------------------
# City ViewSet: provides CRUD for City model
# -----------------------------------------------------------------------------
class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows City to be viewed or edited.
    Requires authentication.
    Supports pagination.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

# -----------------------------------------------------------------------------
# Weather ViewSet: provides CRUD for Weather model
# -----------------------------------------------------------------------------
class WeatherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Weather records to be viewed or edited.
    Supports filtering by city ID using ?city=...
    Requires authentication.
    Supports pagination.
    """
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        queryset = Weather.objects.all()
        city_id = self.request.query_params.get('city')
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        return queryset

# -----------------------------------------------------------------------------
# Frontend dashboard page
# -----------------------------------------------------------------------------
def front_index(request):
    """Render the main HTML dashboard page."""
    return render(request, 'weather/index.html')

# -----------------------------------------------------------------------------
# Frontend data endpoint (PUBLIC ACCESS)
# -----------------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny])  # No token required for frontend
def front_weather_data(request):
    """
    Provide weather data for the frontend dashboard.
    Open to all users (no authentication needed).
    Used by JavaScript on the main page.
    """
    city_id = request.GET.get('city_id')

    if city_id:
        cities = City.objects.filter(id=city_id)
    else:
        cities = City.objects.all()

    data = []
    for city in cities:
        weathers = Weather.objects.filter(city=city).order_by('-date')[:5]
        weather_list = [
            {
                'temperature': w.temperature,
                'description': w.description,
                'date': w.date.strftime('%Y-%m-%d')
            }
            for w in weathers
        ]
        data.append({
            'city_id': city.id,
            'city_name': city.name,
            'country': city.country,
            'weathers': weather_list
        })

    return Response(data)