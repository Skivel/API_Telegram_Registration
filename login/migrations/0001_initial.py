# Generated by Django 4.1.7 on 2023-03-31 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25, verbose_name='User name')),
                ('user_nickname', models.CharField(max_length=255, verbose_name='User nickname')),
                ('user_email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('user_password', models.CharField(max_length=255, verbose_name='User password')),
                ('user_photo', models.FileField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Info',
                'verbose_name_plural': 'Users Info',
            },
        ),
    ]
