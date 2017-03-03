from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import *


class PortfolioView(TemplateView):
    template_name = "portfolio/portfolio.html"


class PortfolioDetailView(DetailView):
    model = PortfolioItem
    template_name = "portfolio/portfolio_details.html"

    def get_context_data(self, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data(**kwargs)
        return context
