from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def index(request):
    return render(
        request,
        'single_pages/index.html'
    )