from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.



class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (('Özel bilgiler', {"fields": ["birth_date","phone"]}),)

class AdminProfile(admin.ModelAdmin):
    list_display = ['title','owner']


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile,AdminProfile)