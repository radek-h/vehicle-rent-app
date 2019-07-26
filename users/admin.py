from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # add_from =
    # form = 
    model = CustomUser
    list_display = ["username", "email", "is_staff"]

admin.site.register(CustomUser)