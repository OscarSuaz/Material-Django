from django.contrib.auth.models import Group,User
from rest_framework import permissions,viewsets
from .serializers import GroupSerilizer,UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerilizer
    permission_classes=[permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]