from django.urls import path
from . import views

urlpatterns = [

    path('flightSearch', views.FlightList, name='flightSearch'),

]