from rest_framework import permissions


class CheckAuthorPermission(permissions.BasePermission):
    """Пермишн для проверки автора поста."""
    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.author == request.user
        return True
