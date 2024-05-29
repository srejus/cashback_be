from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from accounts.models import Account

# Create your views here.
class CouponApi(APIView):
    def get(self,request,id):
        try:
            coupons = Coupon.objects.filter(store__id=id)
        except Coupon.DoesNotExist:
            return Response(
                {
                    "status":"failed",
                    "error":"Invalid StoreID"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        
        serializers = CouponSerializer(coupons,many=True)
        return Response(
            {
                "status":"success",
                "data":serializers.data
            }, status=status.HTTP_200_OK
        )