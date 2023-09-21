from django.shortcuts import render

# Create your views here.
from rest_framework import permissions

class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for authenticated users
        return request.method == 'GET' and request.user.is_authenticated