import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from login.models import UserInfo


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'none.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login_page.html')


@login_required
def user_page(request):
    pass


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = UserInfo(user_name=data['name'], user_nickname=data['nickname'],
                        user_email=data['email'], user_password=data['password'])
        user.save()

        user = User.objects.create_user(username=data['nickname'], first_name=data['name'],
                                        email=data['email'], password=data['password'])
        user.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
