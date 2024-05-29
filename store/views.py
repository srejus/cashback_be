from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
from accounts.models import Account

# Create your views here.
class ListStoreApi(APIView):
    def get(self,request,id=None):
        if id:
            try:
                store = Store.objects.get(id=id)
                serializer = StoreListSerializer(store, many=False)
                return Response(
                    {
                        "status":"success",
                        "data": serializer.data
                    }, status= status.HTTP_200_OK
                )
            except Store.DoesNotExist:
                return Response({
                    "status":"failed",
                    "message":"Store with the given id Does not exists!"
                }, status=status.HTTP_400_BAD_REQUEST)  
            
        location = request.GET.get("location")
        if request.user.is_authenticated:
            try:
                acc = Account.objects.get(user=request.user)
                if not location and acc.place:
                    location=acc.place
            except Exception as e:
                return Response({
                    "status":"failed",
                    "message":str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
            
        if location:
            stores = Store.objects.filter(is_approved=True,location=location)
        else:
            stores = Store.objects.filter(is_approved=True)
        serializer = StoreListSerializer(stores,many=True)
        return Response(
            {
                "status":"success",
                "data": serializer.data
            }, status= status.HTTP_200_OK
        )