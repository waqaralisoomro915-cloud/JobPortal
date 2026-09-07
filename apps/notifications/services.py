from .models import Notification


def notify_application_submitted(application):

    #Notify company employees when a candidate submits an application.


    company = application.job.company

    employees = company.employees.select_related("user")

    for employee in employees:
        Notification.objects.create(
            recipient=employee.user,
            notification_type=(
                Notification.NotificationType.APPLICATION_SUBMITTED
            ),
            title="New Application",
            message=(
                f"A candidate has applied for "
                f"{application.job.title}."
            ),
        )


def notify_application_status_changed(application):

    #Notify candidate when their application status changes.


    Notification.objects.create(
        recipient=application.candidate.user,
        notification_type=(
            Notification.NotificationType.APPLICATION_STATUS_CHANGED
        ),
        title="Application Status Updated",
        message=(
            f"Your application for "
            f"{application.job.title} has been updated to "
            f"{application.status}."
        ),
    )


def notify_interview_scheduled(interview):

    #Notify candidate when an interview is scheduled.


    Notification.objects.create(
        recipient=interview.application.candidate.user,
        notification_type=(
            Notification.NotificationType.INTERVIEW_SCHEDULED
        ),
        title="Interview Scheduled",
        message=(
            f"Your interview for "
            f"{interview.application.job.title} "
            f"has been scheduled for "
            f"{interview.scheduled_at}."
        ),
    )


def notify_interview_rescheduled(interview):
    """
    Notify candidate when an interview is rescheduled.
    """

    Notification.objects.create(
        recipient=interview.application.candidate.user,
        notification_type=(
            Notification.NotificationType.INTERVIEW_RESCHEDULED
        ),
        title="Interview Rescheduled",
        message=(
            f"Your interview for "
            f"{interview.application.job.title} "
            f"has been rescheduled to "
            f"{interview.scheduled_at}."
        ),
    )


def notify_interview_cancelled(interview):
    """
    Notify candidate when an interview is cancelled.
    """

    Notification.objects.create(
        recipient=interview.application.candidate.user,
        notification_type=(
            Notification.NotificationType.INTERVIEW_CANCELLED
        ),
        title="Interview Cancelled",
        message=(
            f"Your interview for "
            f"{interview.application.job.title} "
            f"has been cancelled."
        ),
    )