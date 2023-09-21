from rest_framework import viewsets
from teams.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from teams.views import ReadOnlyPermission  # Import the custom permission class

class TeamViewsets(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [ReadOnlyPermission] 

class TeamViewsets(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class TeamListViewsets(viewsets.ModelViewSet):
    queryset = TeamList.objects.all()
    serializer_class = TeamListSerializer
    permission_classes = [IsAuthenticated]

class PlayerViewsets(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]