from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *
from .models import *
from .util import *

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('name')
    serializer_class = UserSerializer

class BloodRequestViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = blood_request.objects.all()
        serializer = BloodRequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        req = request.data
        recipient = req['recipient']
        r_lat = recipient['latitude']
        r_long = recipient['longitude']
        r_loc = {
            'latitude' : r_lat,
            'longitude' : r_long
        }
        blood_type = recipient['blood_type']
        donors = user.objects.filter(blood_type=blood_type)
        min_dist_donor = donors[0]
        min_duration = 360
        for donor in donors:
            d_lat = donor.latitude
            d_long = donor.longitude
            d_loc = {
                'latitude' : d_lat,
                'longitude' : d_long
            }
            duration = get_min_duration(r_loc, d_loc)
            if duration < min_duration:
                min_duration = duration
                min_dist_donor = donor
                
        blood_request.objects.create(latitude=r_lat, longitude=r_long,
                     blood_type=blood_type, recipient=recipient, donor=donor)
        queryset = blood_request.objects.all()
        serializer = BloodRequestSerializer(queryset, many=True)
        return Response(serializer.data)
    