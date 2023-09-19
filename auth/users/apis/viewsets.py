from rest_framework import viewsets
from users.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from users.views import ReadOnlyPermission  # Import the custom permission class


class UserOrdersViewsets(viewsets.ModelViewSet):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    permission_classes = [IsAuthenticated]