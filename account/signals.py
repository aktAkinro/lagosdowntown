from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.mail import send_mail

User = get_user_model()
# smtp mail service setup
@receiver(post_save, sender=User)
def send_activate_email(sender, instance, created, **kwargs):
    if created:
        message = f"""
            Hello, {instance.first_name}.
            Thank you for signing up on our platform.
            We're happy to have you! 😀🤗😁
            Regards, 
            The Django Team.   
        """
        send_mail(
            subject="Your Account has been created!", 
            message=message, 
            recipient_list=[instance.email],
            from_email="aktakinro@gmail.com"
            )