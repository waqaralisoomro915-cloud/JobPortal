from rest_framework.permissions import BasePermission

from ..accounts.models import User


class CanViewInterview(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.EMPLOYER,
                User.Role.CANDIDATE,
            ]
        )


class CanManageInterview(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.EMPLOYER,
            ]
        )


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )