from django.contrib import admin
from django.urls import path

from login.views import (
    login_view,
    logout_view,
    create_user,
    user_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('user/create', create_user, name='user_create'),
    path('home', user_page, name='home')
]
