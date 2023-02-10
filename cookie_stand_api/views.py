from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStandApi
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandApiSerializer


class CookieStandApiList(ListCreateAPIView):
    queryset = CookieStandApi.objects.all()
    serializer_class = CookieStandApiSerializer


class CookieStandApiDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStandApi.objects.all()
    serializer_class = CookieStandApiSerializer
