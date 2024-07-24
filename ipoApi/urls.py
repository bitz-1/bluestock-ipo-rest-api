from django.contrib import admin
from django.urls import path,include
from ipoApi.views import IpoViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'ipo-list',IpoViewSet)

urlpatterns = [
  path('',include(router.urls))
  
]
