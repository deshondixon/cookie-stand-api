from rest_framework import serializers
from .models import CookieStandApi


class CookieStandApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStandApi
        fields = "__all__"
