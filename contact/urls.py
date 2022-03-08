from django.urls import path, include

from contact.views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]