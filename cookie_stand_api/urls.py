from django.urls import path
from .views import CookieStandApiList, CookieStandApiDetail

urlpatterns = [
    path("", CookieStandApiList.as_view(), name="cookie_stand_api_list"),
    path("<int:pk>/", CookieStandApiDetail.as_view(), name="cookie_stand_api_detail"),
]
