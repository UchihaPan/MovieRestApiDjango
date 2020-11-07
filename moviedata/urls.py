from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from .views import movieviewset
router1=routers.SimpleRouter()
router1.register('',movieviewset)
urlpatterns = [
    path('', include(router1.urls)),
]
