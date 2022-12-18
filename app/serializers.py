from rest_framework import serializers
from app.models import SuperHero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('epic_name', 'secret_identity', 'city')
        model = SuperHero
