from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from main.models import *
from .forms import ReviewForm

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


class AddReview(View):
    """Review's"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Films.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())