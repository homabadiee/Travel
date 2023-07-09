import datetime
import jwt
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .forms import CreateRegisterForm
from rest_framework.authtoken.models import Token
from django.core.cache import cache
from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.exceptions import AuthenticationFailed
from .models import PassengerUser
from .serializers import UserSerializer

# @ratelimit(key='user', rate='5/m', block=True)  # Limit to 5 requests per minute per user
# @ratelimit(key='ip', rate='10/m', block=True)  # Limit to 10 requests per minute per IP
def loginView(request):

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        ip_address = request.META.get('REMOTE_ADDR')

        # Check if password has been tested before
        password_cache_key = f"password_attempt:{email}:{password}"
        if cache.get(password_cache_key):
            return HttpResponseBadRequest("Repeated password not allowed.")

        # Check if too many requests from the same IP within a time period
        ip_cache_key = f"request_count:{ip_address}"
        request_count = cache.get(ip_cache_key)

        if request_count is None:
            cache.set(ip_cache_key, 1, timeout=60)  # Set initial count
        elif request_count >= 5:  # Adjust the number as per your requirement
            messages.info(request, 'Too many requests in a short time period.')
            return render(request, 'login.html')
        else:
            cache.incr(ip_cache_key)  # Increment request count

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
            response = redirect('index')

            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
                'jwt': token
            }

            return response
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')


def registerView(request):
    form = CreateRegisterForm()

    if request.method == 'POST':
        form = CreateRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.info(request, form.error_messages)

    context = {'form': form}

    return render(request, 'register.html', context)


def index(request):
    return render(request, 'index.html')



def editProfile(request):
    return render(request, 'pesonal_info.html')

@api_view(['POST', 'GET'])
def confirmEditProfile(request):
    user = getUser(request)

    if user is not None:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        birthDate = request.POST.get('birthDate')

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'phone': phone,
            'email': email,
            'birthDate': birthDate

        }
        userSerializer = UserSerializer(instance=user, data=data)

        if userSerializer.is_valid():
            userSerializer.save()

    return redirect('index')


def getUser(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    user = PassengerUser.objects.get(id=payload['id'])
    return user


