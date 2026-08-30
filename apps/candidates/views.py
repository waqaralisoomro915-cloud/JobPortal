from rest_framework import viewsets

from .models import Candidate
from .serializers import CandidateSerializer
from .permissions import CanViewCandidate, IsCandidateOwnerOrAdmin
from ..accounts.models import User
from rest_framework.permissions import IsAuthenticated


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == User.ROLE.ADMIN:
            return Candidate.objects.all()

        if user.role in [User.ROLE.HR, User.ROLE.RECRUITER]:
            return Candidate.objects.all()

        return Candidate.objects.filter(user=user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [CanViewCandidate]

        elif self.action in [
            "create",
            "update",
            "partial_update",
            "destroy",
        ]:
            permission_classes = [IsCandidateOwnerOrAdmin]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]