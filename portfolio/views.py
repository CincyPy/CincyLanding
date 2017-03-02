from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import *
from django.utils import timezone
# Create your views here.


class PortfolioView(TemplateView):
    template_name = "portfolio/portfolio.html"


class PortfolioDetails(TemplateView):
    template_name = "portfolio/portfolio_details.html"

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetails, self).get_context_data(**kwargs)
        portid = kwargs.get('pk')
        context['portfolio_details'] = self.get_port_details(portid)
        return context

    def get_port_details(self, portid):
        context = {}
        context['me'] = portid
        return context
