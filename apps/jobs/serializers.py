from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = [
            "id",
            "company",
            "title",
            "description",
            "requirements",
            "job_type",
            "experience_years",
            "location",
            "work_mode",
            "city",
            "salary_min",
            "salary_max",
            "deadline",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, title):
        if not title.strip():
            raise serializers.ValidationError(
                "Please enter a title"
            )
        return title

    def validate_description(self, description):
        if not description.strip():
            raise serializers.ValidationError(
                "Please enter a description"
            )
        return description

    def validate_requirements(self, requirements):
        if not requirements.strip():
            raise serializers.ValidationError(
                "Please enter requirements"
            )
        return requirements

    def validate_experience_years(self, experience_years):
        if experience_years < 0:
            raise serializers.ValidationError(
                "Experience years cannot be negative"
            )
        return experience_years

    def validate_location(self, location):
        if not location.strip():
            raise serializers.ValidationError(
                "Please enter a location"
            )
        return location

    def validate_city(self, city):
        if not city.strip():
            raise serializers.ValidationError(
                "Please enter a city"
            )
        return city