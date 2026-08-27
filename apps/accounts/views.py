from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    LogoutSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)

# REGISTER
class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# LOGIN
class LoginView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer
    permission_classes = [AllowAny]


# LOGOUT
class LogoutView(generics.GenericAPIView):

    serializer_class = LogoutSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response({
            "detail": "Successfully logged out."
        })


# CHANGE PASSWORD
class ChangePasswordView(generics.GenericAPIView):

    serializer_class = ChangePasswordSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response({
            "detail": "Password changed successfully."
        })

# FORGOT PASSWORD
class ForgotPasswordView(generics.GenericAPIView):

    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.user

        token = default_token_generator.make_token(
            user
        )

        uid = user.id

        reset_link = (
            f"http://127.0.0.1:3000/reset-password/"
            f"{uid}/{token}/"
        )

        send_mail(
            subject="Reset your password",
            message=(
                "You requested a password reset.\n\n"
                f"Reset your password here:\n"
                f"{reset_link}\n\n"
                "If you did not request this, ignore this email."
            ),
            from_email=None,
            recipient_list=[
                user.email
            ],
        )

        return Response({
            "detail": "If the account exists, "
                      "a password reset link has been sent."
        })


# RESET PASSWORD
class ResetPasswordView(generics.GenericAPIView):

    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response({
            "detail": "Password reset successfully."
        })