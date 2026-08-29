from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import JobSerializer
from .models import Job
from ..accounts.models import User
from ..companies.permissions import (IsOwner, IsHrOrRecruiterOrOwner, IsHrOrOwner,CanCreateJob)



class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
       user = self.request.user
       if user.role==User.Role.ADMIN:
           return Job.objects.all()
       if user.role == User.Role.CANDIDATE:
           return Job.objects.filter(
               is_active=True,
           )
       return Job.objects.filter(company__employees__user=user).distinct()

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated,CanCreateJob]

        elif self.action in ['update','partial_update']:
            permission_classes = [IsAuthenticated,IsHrOrOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated,IsOwner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission()for permission in permission_classes]

