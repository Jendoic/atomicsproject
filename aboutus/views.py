from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AboutPage


# Create your views here.
class AboutPageListView(ListView):
    model = AboutPage
    context_object_name = "aboutpage_list"
    template_name = "aboutus/aboutpage_list.html"


class AboutPageDetailView(DetailView):
    model = AboutPage
    context_object_name = "aboutus/aboutpage_detail"
    template_name = "aboutus/aboutpage_detail.html"
