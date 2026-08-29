from rest_framework.permissions import BasePermission
from .models import CompanyEmployee


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return CompanyEmployee.objects.filter(
            company=obj.company,
            user=request.user,
            role=CompanyEmployee.Role.OWNER
        )


class IsRecruiter(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return CompanyEmployee.objects.filter(
            company=obj.company,
            user=request.user,
            role=CompanyEmployee.Role.RECRUITER
        ).exists()


class IsHR(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return CompanyEmployee.objects.filter(
            company=obj.company,
            user=request.user,
            role=CompanyEmployee.Role.HR
        ).exists()


class IsHrOrRecruiterOrOwner(BasePermission):
    def has_permission(self, request, view):
        return (
            IsHR().has_permission(request, view)
            or IsRecruiter().has_permission(request, view)
            or IsOwner().has_permission(request, view)
        )