from django.urls import path,include
from users.views import user_views
from users.views import order_views as views
from users.views import product_views


urlpatterns = [
    path('profile/',user_views.getUserProfile,name="user_profile"),
    path('profile/update/',user_views.updateUserProfile,name="user_profile_update"),
    path('myorders/',views.getMyOrders,name="myorders"),
    # path('<str:pk>/',views.getOrderById,name="user-order"),

    path('api/prediction/',product_views.prediction,name="prediction"),
    path('api/results/',product_views.results,name="results"),
    path('api/success/', product_views.payment_success_handle, name='success/'),

    path('api/prediction/<str:pk>/',product_views.getTeam,name="team"),
    path('api/results/<str:pk>/',product_views.viewPaidTeam,name="team"),
]

