from django.views.generic import TemplateView
# Create your views here.


class PortfolioView(TemplateView):
    template_name = "portfolio/portfolio.html"
