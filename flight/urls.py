from django.urls import path
from . import views

urlpatterns = [

    path('flightSearch', views.getFlights, name='flightSearch'),

]