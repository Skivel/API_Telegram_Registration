from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import generics

from .serializers import UserSerializer

from login.models import UserInfo


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login_page.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_page(request):
    user_info = UserInfo.objects.get(user_nickname=request.user)
    context = {
        'user': user_info
    }

    return render(request, 'home_page.html', context)


@csrf_exempt
def create_user(request):
    if request.method == 'POST' and 'image' in request.FILES:
        print(type(request.FILES['image']))
        print(bool(request.FILES['image']))
        image_file = request.FILES['image']

        user = User.objects.create_user(username=request.POST.get('nickname'), first_name=request.POST.get('name'),
                                        password=request.POST.get('password'), email=request.POST.get('email'))
        user.save()

        user_info = UserInfo(user=user, user_name=request.POST.get('name'),
                             user_nickname=request.POST.get('nickname'), user_email=request.POST.get('email'),
                             user_password=request.POST.get('password'), user_photo=image_file)
        user_info.save()
        return JsonResponse({'status': 'success'})

    elif request.method == 'POST':

        user = User.objects.create_user(username=request.POST.get('nickname'), first_name=request.POST.get('name'),
                                        password=request.POST.get('password'), email=request.POST.get('email'))
        user.save()

        user_info = UserInfo(user=user, user_name=request.POST.get('name'),
                             user_nickname=request.POST.get('nickname'), user_email=request.POST.get('email'),
                             user_password=request.POST.get('password'))
        user_info.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def delete_user(request):

    User = get_user_model()

    user = User.objects.get(username=request.user.username)

    user.delete()

    return redirect('login')


# Django register user-list API
class UserList(generics.ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
