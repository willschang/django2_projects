from django.contrib import admin
from .models import UserProfile

# Register your models here.
# class UserProfileAdmin():
#     pass


admin.site.register(UserProfile)
