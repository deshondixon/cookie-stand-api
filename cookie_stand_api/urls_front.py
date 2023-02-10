from django.urls import path
from .views_front import (
    CookieStandApiCreateView,
    CookieStandApiDeleteView,
    CookieStandApiDetailView,
    CookieStandApiListView,
    CookieStandApiUpdateView,
)

urlpatterns = [
    path("", CookieStandApiListView.as_view(), name="cookie_stand_api_list"),
    path("<int:pk>/", CookieStandApiDetailView.as_view(), name="cookie_stand_api_detail"),
    path("create/", CookieStandApiCreateView.as_view(), name="cookie_stand_api_create"),
    path("<int:pk>/update/", CookieStandApiUpdateView.as_view(), name="cookie_stand_api_update"),
    path("<int:pk>/delete/", CookieStandApiDeleteView.as_view(), name="cookie_stand_api_delete"),
]
