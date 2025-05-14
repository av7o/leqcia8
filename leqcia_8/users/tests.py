from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_email = 'testuser@example.com'
        self.password = 'avtoavto'
        self.user = User.objects.create_user(
            username=self.user_email,
            email=self.user_email,
            password=self.password
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': self.user_email,
            'password': self.password
        })
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_logout(self):
        self.client.login(username=self.user_email, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))
        self.assertFalse('_auth_user_id' in self.client.session)

    def test_auth_required_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('dashboard')}")
        self.client.login(username=self.user_email, password=self.password)
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
