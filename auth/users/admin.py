from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','teamName','order_payment_id','isPaid','paidAt','createdAt',]