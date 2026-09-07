from rest_framework.viewsets import ModelViewSet

from .models import Interview
from .serializers import InterviewSerializer
from .permissions import CanViewInterview, CanManageInterview

from ..accounts.models import User


class InterviewViewSet(ModelViewSet):

    serializer_class = InterviewSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == User.Role.ADMIN:
            return Interview.objects.all()

        if user.role == User.Role.EMPLOYER:
            return Interview.objects.filter(
                application__job__company__employees__user=user
            ).distinct()

        if user.role == User.Role.CANDIDATE:
            return Interview.objects.filter(
                application__candidate__user=user
            )

        return Interview.objects.none()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [CanViewInterview]
        else:
            permission_classes = [CanManageInterview]

        return [permission() for permission in permission_classes]
    def perform_create(self, serializer):
        serializer.save(interviewer=self.request.user)