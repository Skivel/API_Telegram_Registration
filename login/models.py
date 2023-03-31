from django.db import models


class UserInfo(models.Model):
    user_name = models.CharField(max_length=25, verbose_name='User name')
    user_nickname = models.CharField(max_length=255, verbose_name='User nickname')
    user_email = models.EmailField(verbose_name='User Email')
    user_password = models.CharField(max_length=255, verbose_name='User password')
    user_photo = models.FileField(upload_to='', blank=True)

    class Meta:
        pass

