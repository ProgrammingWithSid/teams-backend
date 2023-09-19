from rest_framework import viewsets
from users.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class UserOrdersViewsets(viewsets.ModelViewSet):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer
    permission_classes = [IsAuthenticated]
    