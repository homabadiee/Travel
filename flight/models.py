from django.db import models
from user.models import PassengerUser


class Flight(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    total_passengers = models.IntegerField()
    passengers = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    number = models.IntegerField(default=1)
    terminal = models.IntegerField(default=1)
    included_Baggage = models.IntegerField(default=20)
    type = models.CharField(max_length=50, default='economy')
    price = models.IntegerField()
    users = models.ManyToManyField(PassengerUser, through='FlightReservation')


class FlightReservation(models.Model):
    flights = models.ForeignKey(Flight, blank=True, on_delete=models.CASCADE)
    users = models.ForeignKey(PassengerUser, blank=True, on_delete=models.CASCADE)