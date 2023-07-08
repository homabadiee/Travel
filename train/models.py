from django.db import models
from user.models import PassengerUser


class Train(models.Model):
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    total_passengers = models.IntegerField()
    passengers = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    trainNo = models.IntegerField(default=1)
    compNo = models.IntegerField(default=1)
    facility = models.TextField()
    price = models.IntegerField()
    users = models.ManyToManyField(PassengerUser, through='TrainReservation')

class TrainReservation(models.Model):
    trains = models.ForeignKey(Train, blank=True, on_delete=models.CASCADE)
    users = models.ForeignKey(PassengerUser, blank=True, on_delete=models.CASCADE)