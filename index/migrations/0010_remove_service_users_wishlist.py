# Generated by Django 4.0.4 on 2022-06-30 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_remove_service_fav_service_users_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='users_wishlist',
        ),
    ]
