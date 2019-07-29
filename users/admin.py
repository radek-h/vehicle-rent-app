from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add_from =
    # form = 
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('username', 'first_name', 'last_name', 'email')


admin.site.register(CustomUser)