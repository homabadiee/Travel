from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated

@api_view(['POST', 'GET'])
def FlightReserve(request):
    id = request.POST.get('data')
    id2 = request.POST.get('id')
    context = {'id': id}
    print(id)
    print(id2)

    return render(request, 'confirm_reservation.html', {'context': context})


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def FlightList(request):
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
        flight_info = {
                           'id': flight['id'], 'source': flight['source'], 'destination': flight['destination'],
                           'departure_date': flight['departure_date'], 'departure_time': flight['departure_time'],
                           'arrival_time': flight['arrival_time'], 'total_passengers': flight['total_passengers'],
                           'name': flight['name'], 'number': flight['number'], 'terminal': flight['terminal'],
                           'included_Baggage': flight['included_Baggage'], 'type': flight['type'],
                           'price': flight['price']
                       }
        context[i] = flight_info
        i += 1

    return render(request, 'flight_search.html', {'context': context})


@api_view(['POST', 'GET'])
def FlightDetail(request):
    source = request.POST.get('source')
    destination = request.POST.get('destination')
    departure_date = request.POST.get('departure_date')
    flights = Flight.objects.get(source=source, destination=destination, departure_date=departure_date)
    flightSerializer = FlightSerializer(flights, many=False)

    context = {
                   'id': flightSerializer.data['id'], 'source': flightSerializer.data['source'],
                   'destination': flightSerializer.data['destination'],
                   'departure_date': flightSerializer.data['departure_date'],
                   'departure_time': flightSerializer.data['departure_time'],
                   'arrival_time': flightSerializer.data['arrival_time'],
                   'total_passengers': flightSerializer.data['total_passengers'],
                   'name': flightSerializer.data['name'], 'number': flightSerializer.data['number'],
                   'terminal': flightSerializer.data['terminal'],
                   'included_Baggage': flightSerializer.data['included_Baggage'],
                   'type': flightSerializer.data['type'],
                   'price': flightSerializer.data['price']
               }
    return render(request, 'flight_search.html', {'context': context})


@api_view(['POST'])
def FlightCreate(request):
    # source = request.POST.get('source')
    # destination = request.POST.get('destination')
    # departure_date = request.POST.get('departure_date')
    # departure_time = request.POST.get('departure_time')
    # arrival_time = request.POST.get('arrival_time')
    # total_passengers = request.POST.get('total_passengers')
    # name = request.POST.get('name')
    # number = request.POST.get('number')
    # terminal = request.POST.get('terminal')
    # included_Baggage = request.POST.get('included_Baggage')
    # type = request.POST.get('type')
    # price = request.POST.get('price')

    flightSerializer = FlightSerializer(data=request.data)
    if flightSerializer.is_valid():
        flightSerializer.save()

    context = {
                   'id': flightSerializer.data['id'], 'source': flightSerializer.data['source'],
                   'destination': flightSerializer.data['destination'],
                   'departure_date': flightSerializer.data['departure_date'],
                   'departure_time': flightSerializer.data['departure_time'],
                   'arrival_time': flightSerializer.data['arrival_time'],
                   'total_passengers': flightSerializer.data['total_passengers'],
                   'name': flightSerializer.data['name'], 'number': flightSerializer.data['number'],
                   'terminal': flightSerializer.data['terminal'],
                   'included_Baggage': flightSerializer.data['included_Baggage'],
                   'type': flightSerializer.data['type'],
                   'price': flightSerializer.data['price']
               }
    return render(request, 'flight_search.html', {'context': context})


@api_view(['POST'])
def FlightUpdate(request, pk):
    flight = Flight.objects.get(id=pk)
    flightSerializer = FlightSerializer(instance=flight, data=request.data)

    if flightSerializer.is_valid():
        flightSerializer.save()

    context = {
                   'id': flightSerializer.data['id'], 'source': flightSerializer.data['source'],
                   'destination': flightSerializer.data['destination'],
                   'departure_date': flightSerializer.data['departure_date'],
                   'departure_time': flightSerializer.data['departure_time'],
                   'arrival_time': flightSerializer.data['arrival_time'],
                   'total_passengers': flightSerializer.data['total_passengers'],
                   'name': flightSerializer.data['name'], 'number': flightSerializer.data['number'],
                   'terminal': flightSerializer.data['terminal'],
                   'included_Baggage': flightSerializer.data['included_Baggage'],
                   'type': flightSerializer.data['type'],
                   'price': flightSerializer.data['price']
               }
    return render(request, 'flight_search.html', {'context': context})



@api_view(['DELETE'])
def FlightDelete(request, pk):
    flight = Flight.objects.get(id=pk)
    flight.delete()

    flights = Flight.objects.all()
    flightSerializer = FlightSerializer(flights, many=True)

    i = 0
    context = {}

    for flight in flightSerializer.data:
        flight_info = {
                           'id': flight['id'], 'source': flight['source'], 'destination': flight['destination'],
                           'departure_date': flight['departure_date'], 'departure_time': flight['departure_time'],
                           'arrival_time': flight['arrival_time'], 'total_passengers': flight['total_passengers'],
                           'name': flight['name'], 'number': flight['number'], 'terminal': flight['terminal'],
                           'included_Baggage': flight['included_Baggage'], 'type': flight['type'],
                           'price': flight['price']
                       }
        context[i] = flight_info
        i += 1

    return render(request, 'flight_search.html', {'context': context})


