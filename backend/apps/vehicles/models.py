from django.db import models
from apps.users.models import CustomUser

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('fura', 'Fura'),
        ('isuzu', 'Isuzu'),
        ('gazel', 'Gazel'),
        ('ref', 'Ref'),
    ]
    
    driver = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vehicle')
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    plate_number = models.CharField(max_length=20, unique=True)
    capacity_kg = models.IntegerField()
    model_year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.vehicle_type} - {self.plate_number}"