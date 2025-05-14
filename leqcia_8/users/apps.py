from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.db.models.signals import post_save
        from django.contrib.auth.models import User
        from django.core.mail import send_mail
        from django.conf import settings

        def send_welcome_email(sender, instance, created, **kwargs):
            if created and instance.username:
                send_mail(
                    subject='Welcome to Our Site!',
                    message='Hello, thank you for registering at our site!',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[instance.username],
                    fail_silently=True,
                )

        post_save.connect(send_welcome_email, sender=User)
