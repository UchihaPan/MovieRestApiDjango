from rest_framework import serializers
from .models import moviedata

class movieserializer(serializers.ModelSerializer):
    class Meta:
        model=moviedata
        fields=['name','ratings','runtime','movie_type']