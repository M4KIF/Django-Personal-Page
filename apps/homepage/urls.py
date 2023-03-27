

from django.urls import path
from .views import HomepageView, LinkView


app_name='homepage'
urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('', LinkView.as_view(), name='links'),
        ]
