from rest_framework import serializers
from user.models import *
from .models import Hotel



class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = [
                    'destination_city', 'check_in_date', 'check_out_date',
                    'total_passengers', 'address', 'facility', 'price'
                 ]
