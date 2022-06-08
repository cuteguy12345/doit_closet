from django.shortcuts import render
from . models import Best

# Create your views here.
def best_list(request):
    bests = Best.objects.all().order_by('-pk')

    return render(
        request,
        'best/best_list.html',
        {
            'bests':bests
        }
    )

def best_detail(request, pk):
    best = Best.objects.get(pk=pk)

    return render(
        request,
        'best/best_detail.html',
        {
            'best': best,
        }
    )