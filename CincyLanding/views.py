from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class base(TemplateView):
    template_name = "../templates/index.html"

