from django.shortcuts import render
from rest_framework import viewsets
from app.serializers import HeroSerializer
from app.models import SuperHero

# Create your views here.


class SuperHeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = SuperHero.objects.all()