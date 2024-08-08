from django.shortcuts import render
from rest_framework import viewsets
from .serializers import itemSerializer
from .models import item

class itemView(viewsets.ModelViewSet):
    serializer_class=itemSerializer
    queryset=item.objects.all()
