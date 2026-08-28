from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Company, CompanyEmployee
from .serializers import (
    CompanySerializer,
    CompanyEmployeeSerializer
)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "Admin":
            return Company.objects.all()

        return Company.objects.filter(
            employees__user=user
        ).distinct()

    def perform_create(self, serializer):
        company = serializer.save()

        CompanyEmployee.objects.create(
            company=company,
            user=self.request.user,
            role=CompanyEmployee.Role.OWNER
        )


class CompanyEmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyEmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "Admin":
            return CompanyEmployee.objects.all()

        return CompanyEmployee.objects.filter(
            user=user
        )