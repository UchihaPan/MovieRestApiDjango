from rest_framework import serializers
from .models import moviedata

class movieserializer(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=moviedata
        fields=['name','ratings','runtime','movie_type','review','image']