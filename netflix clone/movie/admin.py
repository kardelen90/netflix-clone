from django.contrib import admin
from .models import *
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre,GenreAdmin)