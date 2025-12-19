from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Location
from .serializers import LocationSerializer

# Create your views here.
@api_view(['GET'])
def location_list(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)
