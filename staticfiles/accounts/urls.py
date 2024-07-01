from django.urls import path

from .views import SignupPageView, hx_logout

urlpatterns = [
    path(route="signup/", view=SignupPageView.as_view(), name="signup"),
]


hx_urlpatterns = [
    path(route="hx-logout", view=hx_logout, name="hx-logout"),
]

urlpatterns += hx_urlpatterns
