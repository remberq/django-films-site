from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from main.models import *
from .forms import ReviewForm, RatingForm


class GenreYear:
    """Films genre's and year's premiere"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Films.objects.filter(draft=False).values('year')


class MoviesView(GenreYear, ListView):
    """Film list"""
    model = Films
    queryset = Films.objects.filter(draft=False)
    context_object_name = 'films'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class MovieDetailView(GenreYear, DetailView):
    """Detail description"""
    model = Films
    slug_field = 'url'
    context_object_name = 'films'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context


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


class ActorDetailView(GenreYear, DetailView):
    """Detail information about actor's and director's"""
    model = Actor
    template_name = 'main/actors.html'
    slug_field = 'slug'


class FilterFilmsView(GenreYear, ListView):
    """Films filter"""
    context_object_name = 'films'  # <-- context_obj_name should be the same with MovieView context_obj_name

    def get_queryset(self):
        queryset = Films.objects.filter(
            Q(year__in=self.request.GET.getlist('year')) |
            Q(genres__in=self.request.GET.getlist('genres'))
        ).distinct()  # <-- need to use distinct, or i don't know why queryset has 3 time take the same object
        return queryset


class AddStarRating(View):
    """Добавление рейтинга фильму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Ratio.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
