from rest_framework import serializers
from user.models import *
from .models import Flight



class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = [
                    'id', 'source', 'destination', 'departure_date', 'departure_time',
                    'arrival_time', 'total_passengers', 'name', 'number',
                    'terminal', 'included_Baggage', 'type', 'price'
                 ]
