from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    subject = 'Welcome to our Fan Controller Platform!'
    message = 'Thank you for registering. We are excited to have you.'
    from_email = 'noreply@example.com'
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Sent email to {user_email}"
