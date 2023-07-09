from rest_framework import serializers
from user.models import *
from .models import Suit



class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suit
        fields = [
                    'destination_city', 'check_in_date', 'check_out_date',
                    'total_passengers', 'address', 'facility', 'price'
                 ]
