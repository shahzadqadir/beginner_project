from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    FsharpPageView,
    PythonPageView,
    RacketPageView,
)


urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("fsharp/", FsharpPageView.as_view(), name="fsharp"),
    path("python/", PythonPageView.as_view(), name="python"),
    path("racket/", RacketPageView.as_view(), name="racket"),
    path("", HomePageView.as_view(), name="home"),
]
