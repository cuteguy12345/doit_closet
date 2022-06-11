from django.views.generic import ListView, DetailView

from . models import Best, Category

# Create your views here.
class BestList(ListView):
    model = Best
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(BestList, self).get_context_data()
        context['ctegories'] = Category.objects.all()
        context['no_category_post_count'] = Best.objects.filter(category=None).count()
        return context
    

class BestDetail(DetailView):
    model = Best
    