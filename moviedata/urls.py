from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from .views import movieviewset,actionmovieset
router1=routers.SimpleRouter()
router1.register('',movieviewset)
router1.register('action',actionmovieset)


urlpatterns = [
    path('', include(router1.urls)),
]
