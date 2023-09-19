from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


from rest_framework import status
# Rest Framework Import
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from users.apis.serializers import UserOrderSerializer
from users.models import Team,UserOrder
from django.http import JsonResponse
import razorpay
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from django.shortcuts import render

from rest_framework import permissions

class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for authenticated users
        return request.method == 'GET' and request.user.is_authenticated
    

@api_view(['GET'])
def viewPaidTeam(request,pk):
    user = request.user

    # Retrieve the team with the given UUID for the specific user, or return a 404 if not found
    team = get_object_or_404(Team, uuid=pk)
    
    # Check if the user has ordered this team
    has_ordered_team = UserOrder.objects.filter(user=user, teamName=team,isPaid=True).exists()

    # If the user has ordered the team, retrieve all players in the team using the reverse relationship
    if has_ordered_team:
        players = team.player_set.all()
        
        # Serialize the team and its players
        team_data = {
            'uuid': team.uuid,
            'teamName': team.teamName,
            'image': team.image.url if team.image else None,
            'description': team.description,
            'price': team.price,
        }

        players_data = [
            {
                'uuid': player.uuid,
                'playerName': player.playerName,
                'role': player.role,
                # Add other player fields as needed
            }
            for player in players
        ]

        return JsonResponse({'team': team_data, 'players': players_data})
    else:
        return JsonResponse({'detail': 'User has not ordered this team.'}, status=404)


@api_view(['GET'])
def results(request):

    user = request.user

    # Filter UserOrder objects for the current user where isPaid is True
    paid_orders = UserOrder.objects.filter(user=user, isPaid=True)

    # Serialize the filtered orders
    serializer = UserOrderSerializer(paid_orders, many=True)

    return Response(serializer.data)
    


@api_view(['GET'])
def prediction(request):

    user = request.user

    # Fetch teams that the user has already ordered
    ordered_teams = UserOrder.objects.filter(user=user,isPaid=True).values('teamName')

    predicted_teams = Team.objects.exclude(uuid__in=ordered_teams)
    # print(predicted_teams)
    # Serialize the predicted teams
    predicted_teams_data = []

    for team in predicted_teams:
        team_data = {
            'uuid': team.uuid,
            'teamName': team.teamName,
            'image': team.image.url if team.image else None,
            'description': team.description,
            'price': team.price,
        }
        predicted_teams_data.append(team_data)

    return JsonResponse({'predicted_teams': predicted_teams_data})



@api_view(['POST'])
def getTeam(request, pk):
    user = request.user
    team = get_object_or_404(Team, uuid=pk)
    
    # Convert the price to the nearest whole number (integer)
    amount = round(float(team.price))
    #teamName = request.data['teamName']

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create a Razorpay order
    payment = client.order.create({
        'amount': int(amount * 100),  # Amount should be in paisa (multiplying by 100)
        'currency': 'INR',  # Adjust currency as needed
        'payment_capture': '1',
        
    })

    order = UserOrder.objects.create(teamName=team, 
                                 user = user,
                                 order_payment_id=payment['id'])
    
    serializer = UserOrderSerializer(order)

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)


    # Get the Razorpay payment URL for redirection
    razorpay_payment_url = f'https://checkout.razorpay.com/v1/pay/{order["id"]}'

    response_data = {
        'payment_url': razorpay_payment_url,
        'order_details': order  # Include the order details JSON
    }
    # Return the Razorpay payment URL in the JSON response
    return JsonResponse(response_data)


    # serializer = TeamSerializer(team, many=False)
    # return Response(serializer.data)

@api_view(['POST'])  # Ensure this view only accepts POST requests
@csrf_exempt
def payment_success_handle(request):
    # Parse the JSON data sent by Razorpay
    print(request.data["response"])
    print("\n\n")
    res = json.loads(request.data["response"])


    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    

    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    order = UserOrder.objects.get(order_payment_id=ord_id)

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }
    print(data)
    print("\n\n")
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Verify the webhook event (you can add more validation as needed)
    check = client.utility.verify_payment_signature(data)
    print(check)
    print("\n\n")

    if check is None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)
