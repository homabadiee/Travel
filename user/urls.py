from django.urls import path

from . import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('login', views.loginView, name='login'),
    path('register', views.registerView, name='register'),
    # path('index', views.RegisterView.as_view(), name='register'),
]