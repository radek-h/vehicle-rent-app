from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add_from =
    # form = 
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


admin.site.register(CustomUser)