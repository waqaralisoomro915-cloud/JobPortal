# from rest_framework.permissions import BasePermission
# from ..accounts.models import User
#
#
# class CanViewSkill(BasePermission):
#     def has_permission(self, request, view):
#         return (
#             request.user.is_authenticated
#             and request.user.role in [
#                 User.ROLE.ADMIN,
#                 User.ROLE.EMPLOYER,
#                 User.ROLE.CANDIDATE,
#             ]
#         )
#
#
# class IsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         return (
#             request.user.is_authenticated
#             and request.user.role == User.ROLE.ADMIN
#         )