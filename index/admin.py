from django.contrib import admin

# Register your models here.
from .models import Service
from .models import Image

admin.site.register(Service)
admin.site.register(Image)
