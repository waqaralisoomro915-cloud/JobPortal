from rest_framework import serializers

from .models import Interview
from ..accounts.models import User


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = [
            "id",
            "application",
            "interviewer",
            "scheduled_at",
            "duration",
            "interview_type",
            "meeting_link",
            "status",
            "notes",
            "feedback",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "interviewer",
            "created_at",
            "updated_at",
        ]

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Duration must be greater than 0 minutes."
            )

        return value

    def validate(self, attrs):
        request = self.context["request"]
        user = request.user

        application = attrs.get(
            "application",
            getattr(self.instance, "application", None)
        )

        # Employer can only manage interviews
        # for applications belonging to their company.
        if user.role == User.Role.EMPLOYER:

            company = application.job.company

            is_employee = company.employees.filter(
                user=user
            ).exists()

            if not is_employee:
                raise serializers.ValidationError({
                    "application": (
                        "You cannot create or manage an interview "
                        "for this application."
                    )
                })

        interview_type = attrs.get(
            "interview_type",
            getattr(self.instance, "interview_type", None)
        )

        meeting_link = attrs.get(
            "meeting_link",
            getattr(self.instance, "meeting_link", None)
        )

        if (
            interview_type == Interview.InterviewType.ONLINE
            and not meeting_link
        ):
            raise serializers.ValidationError({
                "meeting_link": (
                    "Meeting link is required for online interviews."
                )
            })

        return attrs