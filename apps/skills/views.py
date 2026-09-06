from rest_framework.viewsets import ModelViewSet
from .models import Skill
from .serializers import SkillSerializer
from .permissions import CanViewSkill, CanManageSkill


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [CanViewSkill]
        else:
            permission_classes = [CanManageSkill]

        return [permission() for permission in permission_classes]