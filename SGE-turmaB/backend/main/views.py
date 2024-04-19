from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, BasePermission

class DeadlineCustomPermission(BasePermission):
    def has_object_permission(self, request, view):
        return 

# Create your views here.
class DeadlineView(ModelViewSet):
    queryset = Deadline.objects.all()
    serializer_class = DeadlineSerializer
    permission_classes = (DeadlineCustomPermission,)

    