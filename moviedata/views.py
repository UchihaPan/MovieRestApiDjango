from django.shortcuts import render
from rest_framework import viewsets
from .models import moviedata
from .serializers import movieserializer
# Create your views here.
class movieviewset(viewsets.ModelViewSet):
    queryset = moviedata.objects.all()
    serializer_class = movieserializer
