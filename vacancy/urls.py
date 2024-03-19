from django.urls import path
from .views import MainPageView

urlpatterns = [
    path('home-page/', MainPageView.as_view())
]
