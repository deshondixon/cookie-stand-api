from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import CookieStandApi


class CookieStandApiListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stand_api/cookie_stand_api_list.html"
    model = CookieStandApi
    context_object_name = "cookie_stand_api"


class CookieStandApiDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stand_api/cookie_stand_api_detail.html"
    model = CookieStandApi
    context_object_name = "cookie_stand_api"


class CookieStandApiUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stand_api/cookie_stand_api_update.html"
    model = CookieStandApi
    fields = "__all__"
    context_object_name = "cookie_stand_api"
    success_url = reverse_lazy("cookie_stand_api_list")


class CookieStandApiCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stand_api/cookie_stand_api_create.html"
    model = CookieStandApi
    fields = "__all__"
    context_object_name = "cookie_stand_api"
    success_url = reverse_lazy("cookie_stand_api_list")


class CookieStandApiDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stand_api/cookie_stands_delete.html"
    model = CookieStandApi
    context_object_name = "cookie_stand_api"
    success_url = reverse_lazy("cookie_stand_api_list")
