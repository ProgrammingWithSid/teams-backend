from django.core.exceptions import RequestDataTooBig
from django.shortcuts import render
from datetime import datetime

from rest_framework import status

# Rest Framework Import
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from users.apis.serializers import UserOrderSerializer
from users.models import UserOrder
from teams.models import Team

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyOrders(request):
    user = request.user
    orders = user.order_set.all()
    serializer = UserOrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request, pk):

    user = request.user
    new_user_order = UserOrder(
            user=user,  
            teamName=Team.objects.get(pk=Team.uuid), 
            isPaid=False,  
        )
    new_user_order.save()

    try:
        order = UserOrder.objects.get(uuid=pk)
        if  order.user == user:
            serializer = UserOrderSerializer(order, many=False)
            return Response(serializer.data)
        # # else :
        # #     if request.method == 'POST':


        #   # Save the new UserOrder instance

        # serializer = TeamSerializer(team, many=False)
        # return Response(serializer.data)

    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)
