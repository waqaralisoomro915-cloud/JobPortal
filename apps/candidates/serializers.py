import re

from rest_framework import serializers
from .models import Candidate
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        read_only_fields = ('user','created_at','updated_at')

    def validate_phone(self, value):
        pattern = r"^\+92\d{10}$"
        if value and not re.match(pattern, value):
            raise serializers.ValidationError("Enter a valid Phone Number")

        if value and not value.startswith("+92"):
            raise serializers.ValidationError(
                "Phone number must start with +92."
            )

        if value and len(value) != 13:
            raise serializers.ValidationError(
                "Phone number must contain 13 characters."
            )

        return value

    def validate_linkedin_url(self, value):
        if value and "linkedin.com" not in value.lower():
            raise serializers.ValidationError(
                "Enter a valid LinkedIn URL."
            )

        return value

    def validate_github_url(self, value):
        if value and "github.com" not in value.lower():
            raise serializers.ValidationError(
                "Enter a valid GitHub URL."
            )

        return value