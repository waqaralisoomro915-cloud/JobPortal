from rest_framework.permissions import BasePermission
from ..accounts.models import User


class CanViewSkill(BasePermission):
    """
    Admin, Employer, and Candidate can view skills.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.EMPLOYER,
                User.Role.CANDIDATE,
            ]
        )


class IsAdmin(BasePermission):
    """
    Only Admin can perform administrative operations.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )


class CanManageSkill(BasePermission):
    """
    Only Admin can create, update, and delete skills.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )