from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(viewname="login")
    template_name = "registration/signup.html"


def hx_logout(request):
    if request.method == "POST":
        logout(request)
        return render(
            request=request,
            template_name="partials/nav_item_list.html",
            context={},
        )
