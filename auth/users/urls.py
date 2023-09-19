from django.urls import path,include
from users.views import user_views
from users.views import order_views as views
from users.views import product_views


urlpatterns = [
    path('profile/',user_views.getUserProfile,name="user_profile"),
    path('profile/update/',user_views.updateUserProfile,name="user_profile_update"),
    path('myorders/',views.getMyOrders,name="myorders"),
    path('<str:pk>/',views.getOrderById,name="user-order"),

    path('prediction/',product_views.prediction,name="prediction"),
    path('results/',product_views.results,name="results"),
    path('success/', product_views.payment_success_handle, name='success/'),

    path('prediction/<str:pk>/',product_views.getTeam,name="team"),
    path('results/<str:pk>/',product_views.viewPaidTeam,name="team"),
]

