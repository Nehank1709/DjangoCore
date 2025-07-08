from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Employee

@receiver(post_save, sender=Employee)
def send_email_it(sender, instance, created, **kwargs):
    if created and instance.department.lower() == "it":
        send_mail(
            subject='Welcome a new member in IT Team',
            message = f"Hi Team, \nPlease welcome {instance.name} to our IT Team. Hope to connect with everyone soon. \n\nThanks \nNeha Kumari\nIT Lead",
            from_email="nksinghnk0@gmail.com",
            recipient_list = ['nknehak098@gmail.com'],
            fail_silently=False,
        )