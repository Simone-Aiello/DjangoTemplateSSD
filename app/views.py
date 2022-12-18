from rest_framework import viewsets, permissions
from app.serializers import HeroSerializer
from app.models import SuperHero
from app.permissions import IsInGroup
# Create your views here.


class SuperHeroViewSet(viewsets.ModelViewSet):
    serializer_class = HeroSerializer
    queryset = SuperHero.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsInGroup]