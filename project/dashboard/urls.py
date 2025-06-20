from django.urls import path
from .views import home, privacy_policy

urlpatterns = [
    path("", home, name="home"),
    path('privacy_policy/',privacy_policy, name='privacy_policy')
]