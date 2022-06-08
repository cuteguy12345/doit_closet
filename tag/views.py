from django.shortcuts import render

# Create your views here.
def best(request):
    return render(
        request,
        'tag/best.html',
    )