from django.urls import path

from . views import IndexView, CalendarView, SearchView, PlaceView
from . views import bunbetsu

urlpatterns = [
    path('', IndexView.as_view()),
    # path('calendar/', CalendarView.as_view()),
    path('separation/', bunbetsu),
    # path('search/', SearchView.as_view()),
    path('place/', PlaceView.as_view()),
]