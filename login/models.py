from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    user_name = models.CharField(max_length=25, verbose_name='User name', blank=True)
    user_nickname = models.CharField(max_length=255, verbose_name='User nickname', blank=True)
    user_email = models.EmailField(verbose_name='User Email', blank=True)
    user_password = models.CharField(max_length=255, verbose_name='User password', blank=True)
    user_photo = models.FileField(upload_to='users_image', blank=True)

    class Meta:
        verbose_name = 'User Info'
        verbose_name_plural = 'Users Info'

    def __str__(self):
        return self.user_nickname

