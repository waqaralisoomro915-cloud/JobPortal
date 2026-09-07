from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application

        fields = (
            "id",
            "job",
            "cover_letter",
            "resume",
            "status",
            "applied_at",
            "updated_at",
        )

        read_only_fields = (
            "id",
            "status",
            "applied_at",
            "updated_at",
        )