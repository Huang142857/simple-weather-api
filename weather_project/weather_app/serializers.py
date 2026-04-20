from rest_framework import serializers
from .models import City, Weather

# Serializer for City model
# Handles validation and data conversion for City API
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'  # Include all fields from the model


# Serializer for Weather model
# Converts Weather data to/from JSON format
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'