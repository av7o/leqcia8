import random
import string
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length)).capitalize()

class Command(BaseCommand):
    help = 'Create 10 new users with random unique first and last names and password "avtoavto"'

    def handle(self, *args, **kwargs):
        created = 0
        attempts = 0
        while created < 10 and attempts < 50:
            first_name = random_name()
            last_name = random_name()
            email = f'{first_name.lower()}.{last_name.lower()}@example.com'
            if not User.objects.filter(username=email).exists():
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password='avtoavto',
                    first_name=first_name,
                    last_name=last_name
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Created user: {email} ({first_name} {last_name})'
                ))
                created += 1
            attempts += 1
        if created < 10:
            self.stdout.write(self.style.WARNING(
                f'Only {created} users created due to uniqueness constraints.'
            ))