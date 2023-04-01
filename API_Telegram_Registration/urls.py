from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from API_Telegram_Registration import settings
from login.views import (
    login_view,
    logout_view,
    create_user,
    delete_user,
    user_page,
    UserList
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('user/create', create_user, name='user-create'),
    path('user/delete', delete_user, name='user-delete'),
    path('home', user_page, name='home'),
    path('api/v1/users', UserList.as_view(), name='user-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)