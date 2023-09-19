from users.apis.serializers import CustomUserCreateSerializer
from djoser.views import UserCreateView
import logging

logger = logging.getLogger(__name__)

class CustomUserCreateView(UserCreateView):
    serializer_class = CustomUserCreateSerializer

    def create(self, request, *args, **kwargs):
        logger.info("User created with CustomUserCreateSerializer")
        return super().create(request, *args, **kwargs)
