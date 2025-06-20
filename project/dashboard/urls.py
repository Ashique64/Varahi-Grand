from django.urls import path
from .views import home, privacy_policy, terms_and_conditions, refund_policy

urlpatterns = [
    path("", home, name="home"),
    path('privacy_policy/',privacy_policy, name='privacy_policy'),
    path('terms_and_conditions/',terms_and_conditions, name='terms_and_conditions'),
    path('refund_policy/',refund_policy, name='refund_policy'),
]