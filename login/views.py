import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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


def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = UserInfo(user_name=data['name'], user_nickname=data['nickname'], user_email=data['email'],
                        password=data['password'])
        user.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
