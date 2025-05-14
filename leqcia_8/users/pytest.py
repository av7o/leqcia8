import pytest
from django.contrib.auth.models import User
from django.urls import reverse

@pytest.mark.django_db
def test_user_login(client):
    user = User.objects.create_user(username='testuser@example.com', password='avtoavto')
    response = client.post(reverse('login'), {
        'username': 'testuser@example.com',
        'password': 'avtoavto'
    })
    assert response.status_code == 302
    assert response.url == reverse('dashboard')

@pytest.mark.django_db
def test_user_logout(client):
    user = User.objects.create_user(username='testuser@example.com', password='avtoavto')
    client.login(username='testuser@example.com', password='avtoavto')
    response = client.get(reverse('logout'))
    assert response.status_code == 302
    assert response.url == reverse('login')

@pytest.mark.django_db
def test_dashboard_requires_auth(client):
    response = client.get(reverse('dashboard'))
    login_url = reverse('login') + '?next=' + reverse('dashboard')
    assert response.status_code == 302
    assert response.url.endswith('?next=/dashboard/')