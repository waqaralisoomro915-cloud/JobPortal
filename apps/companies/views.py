from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import (IsOwner,IsRecruiter,IsHR,IsHrOrRecruiterOrOwner)
from ..accounts.models import User
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

        if user.role == User.Role.ADMIN:
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


    def get_permissions(self):

        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated,IsHrOrRecruiterOrOwner]

        elif self.action in [
            "create",
            "update",
            "partial_update",
            "destroy"
        ]:
            permission_classes = [IsAuthenticated,IsOwner]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]




