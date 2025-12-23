from rest_framework import serializers
from .models import Location
from django.contrib.gis.geos import Point

class LocationSerializer(serializers.ModelSerializer): 
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True) 
    class Meta:
        model = Location
        fields = ['id', 'name', 'location', 'latitude', 'longitude']

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        
        point = Point(longitude,latitude)