from django.shortcuts import render

# Create your views here.


def home(request):
    print("Home view called") 
    return render(request, 'index.html')