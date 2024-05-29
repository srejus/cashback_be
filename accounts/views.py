import random
import string
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class GetUserApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        try:
            acc = Account.objects.get(user=request.user)
            serializer = AccountSerializer(acc,many=False)
            return Response(
                {
                    "status":"success",
                    "data":serializer.data
                },
                status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "status":"error",
                    "message":e
                },status=status.HTTP_400_BAD_REQUEST)
        
    
class LoginApi(APIView):
    def post(self,request):
        username = request.data.get("username")
        otp = request.data.get("otp")
        if not otp and not username:
            return Response(
                {"status":"failed",
                 "message":"'username' or 'otp' is required"
                },status=status.HTTP_400_BAD_REQUEST
            )
    
        if username and not otp:
            acc = Account.objects.filter(user__username=username)
            if not acc.exists():
                return Response(
                    {"status":"failed",
                    "message":"Incorrect email"
                    },status=status.HTTP_400_BAD_REQUEST
                )
            
            otp_code = ''.join(random.choices(string.digits, k=4))
            print("OTP : ",otp_code)
            acc = acc.first()
            acc.otp = otp_code
            acc.otp_created_at = timezone.now()
            acc.save()
            return Response(
                {
                    "status":"success",
                    "message":"OTP sent successfully!"
                }, status=status.HTTP_200_OK
            )
        elif otp and username:
            acc = Account.objects.filter(user__username=username)
            if not acc.exists():
                return Response(
                    {"status":"failed",
                    "message":"Incorrect email"
                    },status=status.HTTP_400_BAD_REQUEST
                )
            acc = acc.first()
            if otp != str(acc.otp):
                return Response(
                    {"status":"failed",
                    "message":"Incorrect OTP"
                    },status=status.HTTP_400_BAD_REQUEST
                )
            
            if timezone.now() - acc.otp_created_at <= timedelta(minutes=5):
                login(request,acc.user)
                # Generate tokens
                refresh = RefreshToken.for_user(acc.user)
                access = refresh.access_token
                return Response(
                    {
                       "access_token":str(access),
                       "refresh_token":str(refresh)
                    },
                    status=status.HTTP_200_OK
                )
        else:
             return Response(
                {"status":"failed",
                 "message":"'username' is required"
                },status=status.HTTP_400_BAD_REQUEST
            )
        

class RegisterApi(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "status":"success",
                        "message":"Account Created Successfully!"
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {
                        "status":"failed",
                        "errors":str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            {
                "status":"failed",
                "errors":serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )