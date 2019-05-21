from django.contrib import admin
from .models import UserInfo


@admin.register(UserInfo)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
