from django.shortcuts import render
from django.views.generic import ListView

from .models import HomePage


# Create your views here.
class HomePageView(ListView):
    model = HomePage
    template_name = "home.html"
