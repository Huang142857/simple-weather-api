from django.contrib import admin
from .models import City, Weather

# Register City model to admin panel
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')

# Register Weather model to admin panel
@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'temperature', 'description', 'date')