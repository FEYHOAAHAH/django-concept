from django.shortcuts import render


# Create your views here.

def app_concept(request):
    return render(request, 'index.html')
