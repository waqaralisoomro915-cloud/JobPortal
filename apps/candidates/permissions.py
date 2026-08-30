from rest_framework.permissions import BasePermission

from ..accounts.models import User


class IsCandidate(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE.CANDIDATE
        )


class IsCandidateOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == User.ROLE.ADMIN
            or obj.user == request.user
        )
class CanViewCandidate(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.role in [
                User.ROLE.ADMIN,
                User.ROLE.HR,
                User.ROLE.RECRUITER,
                User.ROLE.CANDIDATE,
            ]
        )

    def has_object_permission(self, request, view, obj):
        user = request.user

        return (
            user.role in [
                User.ROLE.ADMIN,
                User.ROLE.HR,
                User.ROLE.RECRUITER,
            ]
            or obj.user == user
        )