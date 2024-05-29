from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['otp','otp_created_at']

    
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    full_name = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'full_name', 'phone', 'place', 'referral_code']

    def create(self, validated_data):
        # Extract the fields for the User model
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'email': validated_data.pop('email'),
        }
        
        # Create the User object
        user = User.objects.create_user(**user_data)
        
        # Create the Account object and link it to the User object
        account = Account.objects.create(user=user, **validated_data)
        
        return account