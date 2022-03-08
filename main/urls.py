from django.urls import path, include
from .views import MoviesView, MovieDetailView, AddReview, ActorDetailView, FilterFilmsView, AddStarRating, SearchFilm

urlpatterns = [
    path('', MoviesView.as_view()),
    path('filter/', FilterFilmsView.as_view(), name='filter'),
    path('search/', SearchFilm.as_view(), name='search'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<slug:slug>', ActorDetailView.as_view(), name='actors_view'),

]
