from rest_framework.permissions import BasePermission


class CanViewNotification(BasePermission):
    """
    Authenticated users can view their own notifications.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.recipient == request.user


class CanManageNotification(BasePermission):
    """
    Authenticated users can manage their own notifications.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.recipient == request.user