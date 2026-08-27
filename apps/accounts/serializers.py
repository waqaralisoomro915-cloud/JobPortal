from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

# REGISTER
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    password_confirm = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "password_confirm",
        ]

    def validate(self, attrs):

        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({
                "password_confirm": "Passwords do not match."
            })

        return attrs

    def create(self, validated_data):

        validated_data.pop("password_confirm")

        password = validated_data.pop("password")

        user = User.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=password,
            role=User.Role.CANDIDATE
        )

        return user

# LOGIN / JWT

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["role"] = user.role

        return token

# LOGOUT
class LogoutSerializer(serializers.Serializer):

    refresh = serializers.CharField()

    def validate(self, attrs):

        try:
            self.token = RefreshToken(attrs["refresh"])

        except Exception:
            raise serializers.ValidationError({
                "refresh": "Invalid or expired refresh token."
            })

        return attrs

    def save(self, **kwargs):

        self.token.blacklist()

# CHANGE PASSWORD

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(
        write_only=True
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    new_password_confirm = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        user = self.context["request"].user

        if not user.check_password(
            attrs["old_password"]
        ):
            raise serializers.ValidationError({
                "old_password": "Old password is incorrect."
            })

        if attrs["new_password"] != attrs["new_password_confirm"]:
            raise serializers.ValidationError({
                "new_password_confirm": "Passwords do not match."
            })

        if user.check_password(
            attrs["new_password"]
        ):
            raise serializers.ValidationError({
                "new_password":
                    "New password must be different from old password."
            })

        return attrs

    def save(self, **kwargs):

        user = self.context["request"].user

        user.set_password(
            self.validated_data["new_password"]
        )

        user.save()

        return user

# FORGOT PASSWORD

class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):

        try:
            self.user = User.objects.get(
                email=value
            )

        except User.DoesNotExist:
            raise serializers.ValidationError(
                "No account exists with this email."
            )

        return value


# RESET PASSWORD

class ResetPasswordSerializer(serializers.Serializer):

    uid = serializers.CharField()

    token = serializers.CharField()

    new_password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    new_password_confirm = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        # Find user
        try:
            user = User.objects.get(
                id=attrs["uid"]
            )

        except User.DoesNotExist:
            raise serializers.ValidationError({
                "uid": "Invalid user."
            })

        # Validate reset token
        if not default_token_generator.check_token(
            user,
            attrs["token"]
        ):
            raise serializers.ValidationError({
                "token": "Invalid or expired token."
            })

        # Confirm new password
        if (
            attrs["new_password"]
            != attrs["new_password_confirm"]
        ):
            raise serializers.ValidationError({
                "new_password_confirm":
                    "Passwords do not match."
            })

        # Don't allow old password
        if user.check_password(
            attrs["new_password"]
        ):
            raise serializers.ValidationError({
                "new_password":
                    "New password must be different from old password."
            })

        self.user = user

        return attrs

    def save(self, **kwargs):

        user = self.user

        user.set_password(
            self.validated_data["new_password"]
        )

        user.save()

        return user