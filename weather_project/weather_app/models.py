from django.db import models

# city model
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# weather record model
class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="weathers")
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.name} - {self.temperature}°C"
