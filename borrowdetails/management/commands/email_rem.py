from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from borrowdetails.models import BorrowModel

class Command(BaseCommand):
    help = 'Send event reminder emails 5 days before the event'

    def handle(self, *args, **kwargs):
        # Calculate the date 5 days from now
        five_days_from_now = timezone.now() + timezone.timedelta(days=5)

        # Query events that are 5 days from now
        user_to_remind = BorrowModel.objects.filter(event_date=five_days_from_now)

        for that_user in user_to_remind:
            subject = 'Event Reminder'
            message = f"Don't forget about the return date of book '{that_user.book}' is on {that_user.date_of_return}.Fine of Rs.2 will be added every day after due date"
            from_email = 'yourlibrary@gmail.com'
            recipient_list = [that_user.user.email]

            send_mail(subject, message, from_email, recipient_list)
            self.stdout.write(self.style.SUCCESS(f'Sent reminder email to {that_user.user.email}'))