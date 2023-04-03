

from django.urls import path
from .views import HomeView, LinkView


app_name='homepage'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', LinkView.as_view(), name='links'),
        ]
