from rest_framework import serializers
from . models import Company,CompanyEmployee

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "company_name",
            "description",
            "logo",
            "website",
            "industry",
            "company_size",
            "location",
            "founded_year",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEmployee
        fields = [
            "id",
            "company",
            "user",
            "role",
            "joined_at",
        ]
        read_only_fields = [
            "id",
            "joined_at",
        ]
