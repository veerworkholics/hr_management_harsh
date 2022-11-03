from django.contrib import admin
from .models import Customuser

# Register your models here.

class User(admin.ModelAdmin):
 list_display = ['first_name']

admin.site.register(Customuser,User)
