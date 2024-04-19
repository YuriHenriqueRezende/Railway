from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

rounter = DefaultRouter()
rounter.register(r'deadline', DeadlineView)

urlpatterns = rounter.urls