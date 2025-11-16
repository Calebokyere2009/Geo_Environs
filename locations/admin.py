from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import PointOfInterest

@admin.register(PointOfInterest)
class PointOfInterestAdmin(GISModelAdmin):
    list_display = ('name', 'location', 'created_at')
    search_fields = ('name',)
