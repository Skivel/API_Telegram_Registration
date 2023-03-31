from django.contrib import admin
from django.urls import path

from login.views import (
    login_view,
    create_user
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('user/create', create_user, name='user_create')
]
