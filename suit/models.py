from django.db import models
from user.models import PassengerUser

class Suit(models.Model):
    destination_city = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_passengers = models.IntegerField()
    address = models.TextField()
    facility = models.TextField()
    price = models.IntegerField()
    users = models.ManyToManyField(PassengerUser, through='SuitReservation')


class SuitReservation(models.Model):
    suits = models.ForeignKey(Suit, blank=True, on_delete=models.CASCADE)
    users = models.ForeignKey(PassengerUser, blank=True, on_delete=models.CASCADE)