from django.db import models
from user.models import PassengerUser

class Hotel(models.Model):
    destination_city = models.CharField(max_length=50)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_passengers = models.IntegerField()
    address = models.TextField()
    facility = models.TextField()
    price = models.IntegerField()
    users = models.ManyToManyField(PassengerUser, through='HotelReservation')

class HotelReservation(models.Model):
    hotels = models.ForeignKey(Hotel, blank=True, on_delete=models.CASCADE)
    users = models.ForeignKey(PassengerUser, blank=True, on_delete=models.CASCADE)