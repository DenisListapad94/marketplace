from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import CustomUser,UserRating

admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserRating)