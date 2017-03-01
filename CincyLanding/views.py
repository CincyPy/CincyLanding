from django.views import generic
from portfolio.models import PortfolioItem, Package
# Create your views here.

class base(generic.ListView):
    template_name = "../templates/index.html"
    context_object_name = 'portfolio_item_list'

    def get_queryset(self):
        return PortfolioItem.objects.order_by('project_name')