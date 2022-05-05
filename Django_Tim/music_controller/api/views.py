from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room
from django.shortcuts import render

# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

