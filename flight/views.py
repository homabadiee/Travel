from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *


@api_view(['GET'])
def getFlights(request):
    # TODO : check input_passengers <= passengers + total_passengers
    flights = Flight.objects.all()
    flightSerializer = FlightSerializer(flights, many=True)

    i = 0
    context = {}

    for flight in flightSerializer.data:
        flight_info = {'source': flight['source'], 'destination': flight['destination'],
                       'departure_date': flight['departure_date'], 'departure_time': flight['departure_time'],
                       'arrival_time': flight['arrival_time'], 'total_passengers': flight['total_passengers'],
                       'name': flight['name'], 'number': flight['number'], 'terminal': flight['terminal'],
                       'included_Baggage': flight['included_Baggage'], 'type': flight['type'],
                       'price': flight['price']
                       }
        context[i] = flight_info
        i += 1

    return render(request, 'flight-index.html', {'context': context})
