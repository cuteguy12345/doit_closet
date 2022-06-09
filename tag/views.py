from django.views.generic import ListView, DetailView
from . models import Best

# Create your views here.
class BestList(ListView):
    model = Best
    ordering = '-pk'
    template_name = 'best/best_list.html'

class BestDetail(DetailView):
    model = Best
    template_name = 'best/best_detail.html'