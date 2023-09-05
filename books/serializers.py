from rest_framework import serializers
from .models import CustomUser,BookModel

class UserSer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email','username','password','BorrowCount','is_superuser']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
class BookSer(serializers.ModelSerializer):
    available=serializers.BooleanField(read_only=True)
    class Meta:
        model=BookModel
        fields="__all__"