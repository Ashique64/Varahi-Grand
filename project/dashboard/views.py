from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')