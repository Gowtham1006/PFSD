# models.py
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.flight_number} - {self.source} to {self.destination}"


# models.py
from django.db import models

class FormData(models.Model):
    from_field = models.CharField(max_length=100)
    to_field = models.CharField(max_length=100)
    date = models.DateField()

class Ticket(models.Model):
    from1=models.CharField(max_length=100)
    to=models.CharField(max_length=100)