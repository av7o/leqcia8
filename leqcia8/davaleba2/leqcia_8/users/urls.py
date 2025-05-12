from django.urls import path
from .views import register_view, login_view, custom_logout_view, home_view, dashboard_view

urlpatterns = [
    path('', home_view, name='home'),  # Set home_view for the root URL
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),  # Add dashboard URL
]