# Django Import 
from django.shortcuts import render

# Rest Framework Import
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from users.apis.serializers import CustomUserCreateSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user =request.user 
    serializer = CustomUserCreateSerializer(user,many = False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user =request.user 
    serializer = CustomUserCreateSerializer(user,many = False)
    data = request.data
    user.name = data['name']
    user.email = data['email']
    user.save()
    return Response(serializer.data)

