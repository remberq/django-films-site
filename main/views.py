from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from main.models import *


class MoviesView(ListView):
    """Film list"""
    model = Films
    queryset = Films.objects.filter(draft=False)
    context_object_name = 'films'


class MovieDetailView(DetailView):
    """Detail description"""
    model = Films
    slug_field = 'url'
    context_object_name = 'films'
