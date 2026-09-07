from rest_framework.permissions import BasePermission
from ..accounts.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.ADMIN
        )


class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.CANDIDATE
        )


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.EMPLOYER
        )


class CanCreateApplication(BasePermission):
    """
    Only candidates can create applications.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.CANDIDATE
        )


class CanViewApplication(BasePermission):
    """
    Admin, employer, and candidate can view applications.
    Ownership/filtering should be handled in the ViewSet.
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


class CanManageApplication(BasePermission):
    """
    Admin and employer can manage applications.
    Candidate cannot change an application after submission.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.Role.ADMIN,
                User.Role.EMPLOYER,
            ]
        )