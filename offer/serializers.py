from rest_framework import serializers
from .models import *
from store.serializers import StoreListSerializer


class CouponSerializer(serializers.ModelSerializer):
    store = StoreListSerializer()
    class Meta:
        model = Coupon
        fields = "__all__"

