from rest_framework.viewsets import ModelViewSet

from .models import Application
from .serializers import ApplicationSerializer

from ..accounts.models import User
from .permissions import (
    CanCreateApplication,
    CanViewApplication,
    CanManageApplication,
)


class ApplicationViewSet(ModelViewSet):

    serializer_class = ApplicationSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Application.objects.none()

        # Admin can see everything
        if user.role == User.Role.ADMIN:
            return Application.objects.all()

        # Candidate can see only their own applications
        if user.role == User.Role.CANDIDATE:
            return Application.objects.filter(
                candidate__user=user
            )

        # Employer can see applications
        # for jobs belonging to their company
        if user.role == User.Role.EMPLOYER:
            return Application.objects.filter(
                job__company__employees__user=user
            ).distinct()

        return Application.objects.none()

    def get_permissions(self):

        if self.action == "create":
            permission_classes = [CanCreateApplication]

        elif self.action in ["list", "retrieve"]:
            permission_classes = [CanViewApplication]

        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [CanManageApplication]

        else:
            permission_classes = [CanViewApplication]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(
            candidate=self.request.user.candidate
        )