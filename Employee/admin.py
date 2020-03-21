from django.contrib import admin
from .models import *

@admin.register(Profile)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('user','user_type')


