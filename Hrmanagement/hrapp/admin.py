from django.contrib import admin
from .models import Customuser,Role

# Register your models here.

class User(admin.ModelAdmin):
 list_display = ['first_name']

admin.site.register(Customuser,User)

@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display=['id','role_name','status','created_at','updated_at']