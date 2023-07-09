from rest_framework import serializers
from user.models import *
from .models import Train



class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Train
        fields = [
                    'source', 'destination', 'departure_date', 'departure_time', 'arrival_date',
                    'arrival_time', 'name', 'trainNo', 'compNo', 'facility', 'price'
                 ]
