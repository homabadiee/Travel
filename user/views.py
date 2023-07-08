import datetime
import jwt
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CreateRegisterForm


# @ratelimit(key='user', rate='5/m', block=True)  # Limit to 5 requests per minute per user
# @ratelimit(key='ip', rate='10/m', block=True)  # Limit to 10 requests per minute per IP
def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

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