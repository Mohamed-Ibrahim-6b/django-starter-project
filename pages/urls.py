from django.urls import path

from .views import HomePageView

app_name = "pages"

urlpatterns = [
    path(route="", view=HomePageView.as_view(), name="home"),
]
