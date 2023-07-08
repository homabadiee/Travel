from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated

@permission_classes([IsAuthenticated])
def getFlights(request):
    # TODO : check input_passengers <= passengers + total_passengers
    # TODO : check data is not empty
    source = request.POST.get('source')
    destination = request.POST.get('destination')
    departure_date = request.POST.get('departure_date')
    # passengers_num = request.POST.get('passengers')


    flights = Flight.objects.filter(source=source, destination=destination, departure_date=departure_date)
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

    return render(request, 'flight_search.html', {'context': context})
