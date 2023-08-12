from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from api.models import *
import json


@csrf_exempt
def SignIn(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        userPass = request.POST['userPass']

        if userName == 'Saman' and userPass == '1381':
            return render(request, 'pages/singin.html', {'errorUserPass': 'Welcome'})
        else:
            return render(request, 'pages/singin.html', {'errorUserPass': 'Error'})
    return render(request, 'pages/singin.html')
