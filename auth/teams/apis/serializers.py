from django.contrib.auth.models import Permission
from rest_framework import serializers
from teams.models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamList
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta:
        model = Player
        fields = '__all__'
