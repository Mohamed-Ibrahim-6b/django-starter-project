from django.urls import path

from .views import AboutPageView, HomePageView

app_name = "pages"

urlpatterns = [
    path(route="about/", view=AboutPageView.as_view(), name="about"),
    path(route="", view=HomePageView.as_view(), name="home"),
]
