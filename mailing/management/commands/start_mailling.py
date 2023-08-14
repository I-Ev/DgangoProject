from django.core.management import BaseCommand
from django.core.mail import EmailMessage

from mailing.models import Client


class Command(BaseCommand):
    """Sends out emails to clients."""

    def handle(self, *args, **options):
        # Get all clients.
        clients = Client.objects.all()

        # Create a new email message.
        message = EmailMessage()
        message.subject = 'This is a test email.'
        message.body = 'This is the body of the email.'

        # Add all clients to the email message.
        for client in clients:
            message.to.append(client.email)

        # Send the email message.
        message.send()
