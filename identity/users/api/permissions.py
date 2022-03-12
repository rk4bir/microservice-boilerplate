from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.is_staff


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        """Check if user has object permission"""
        return request.user == obj


class IsOwnerOrAdminOrStaff(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser or request.user.is_staff
