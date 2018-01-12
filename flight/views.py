from django.views import generic
from .models import Flight

class IndexView(generic.ListView):
    template_name = 'flight/index.html'
    context_object_name = 'all_flights'

    def get_queryset(self):
        return Flight.objects.all()


class DetailView(generic.DetailView):
    model = Flight
    template_name = 'flight/detail.html'
