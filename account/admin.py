from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from store.models import User

# Register your models here.
admin.site.register(User)
