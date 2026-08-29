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
        ).exists()


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
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return CompanyEmployee.objects.filter(
            company=obj.company,
            user=request.user,
            role__in=[
                CompanyEmployee.Role.OWNER,
                CompanyEmployee.Role.HR,
                CompanyEmployee.Role.RECRUITER,
            ]
        ).exists()


class IsHrOrOwner(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return CompanyEmployee.objects.filter(
            company=obj.company,
            user=request.user,
            role__in=[
                CompanyEmployee.Role.OWNER,
                CompanyEmployee.Role.HR,
            ]
        ).exists()



class CanCreateJob(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        company_id = request.data.get("company")

        if not company_id:
            return False

        return CompanyEmployee.objects.filter(
            company_id=company_id,
            user=request.user,
            role__in=[
                CompanyEmployee.Role.OWNER,
                CompanyEmployee.Role.HR,
                CompanyEmployee.Role.RECRUITER,
            ]
        ).exists()