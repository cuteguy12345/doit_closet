from django.views.generic import ListView, DetailView
from . models import Best

# Create your views here.
class BestList(ListView):
    model = Best
    ordering = '-pk'
    

class BestDetail(DetailView):
    model = Best
    