from rest_framework import serializers
from .models import BorrowModel

class BorrowSer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    book=serializers.CharField(read_only=True)
    class Meta:
        model=BorrowModel
        fields="__all__"
