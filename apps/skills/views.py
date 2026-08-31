# from rest_framework import viewsets
#
# from .models import Skill
# from .serializers import SkillSerializer
# from .permissions import CanViewSkill, IsAdmin
#
#
# class SkillViewSet(viewsets.ModelViewSet):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#
#     def get_permissions(self):
#         if self.action in ["list", "retrieve"]:
#             permission_classes = [CanViewSkill]
#
#         elif self.action in [
#             "create",
#             "update",
#             "partial_update",
#             "destroy",
#         ]:
#             permission_classes = [IsAdmin]
#
#         else:
#             permission_classes = [CanViewSkill]
#
#         return [permission() for permission in permission_classes]

from django.http import HttpResponse
def skills(request):
    return HttpResponse("Hello, world. You're at the polls app.")