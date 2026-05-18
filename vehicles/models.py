from django.db import models
from clients.models import Client


class Vehicle(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicles')
    plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.brand} {self.vehicle_model} {self.plate}'
