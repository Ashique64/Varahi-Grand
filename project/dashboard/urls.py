from django.urls import path
from .views import home, privacy_policy, terms_and_conditions

urlpatterns = [
    path("", home, name="home"),
    path('privacy_policy/',privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/',terms_and_conditions, name='terms_and_conditions'),
]