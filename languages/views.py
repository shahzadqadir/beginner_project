from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PythonPageView(TemplateView):
    template_name = "python.html"


class FsharpPageView(TemplateView):
    template_name = "fsharp.html"


class RacketPageView(TemplateView):
    template_name = "racket.html"
