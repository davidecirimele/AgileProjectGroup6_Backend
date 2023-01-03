from rest_framework import permissions

from home.models import Student


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin_group').exists()


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user and obj.owner == request.user

class IsHe(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user and obj.username == request.user