from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import City, Weather
from .serializers import CitySerializer, WeatherSerializer

# 原有 ViewSet 保持不变
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        queryset = Weather.objects.all()
        city_id = self.request.query_params.get('city')
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        return queryset

def front_index(request):
    """Render the front-end page for weather display"""
    return render(request, 'weather/index.html')

@api_view(['GET'])
def front_weather_data(request):
    """A weather data interface for the front end to call"""
    city_id = request.GET.get('city_id')
    data = []
    cities = City.objects.all()
    if city_id:
        cities = cities.filter(id=city_id)
    
    for city in cities:
        weathers = Weather.objects.filter(city=city).order_by('-date')[:5] 
        weather_list = [{
            'temperature': w.temperature,
            'description': w.description,
            'date': w.date.strftime('%Y-%m-%d')
        } for w in weathers]
        data.append({
            'city_id': city.id,
            'city_name': city.name,
            'country': city.country,
            'weathers': weather_list
        })
    return Response(data)