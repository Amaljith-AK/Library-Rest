from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.response import Response
from .serializers import BorrowSer
from books.models import BookModel
from .models import BorrowModel
from datetime import date
from rest_framework.decorators import action

# Create your views here.




class BorrowMVS(ModelViewSet):
    serializer_class=BorrowSer
    queryset=BorrowModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    # def list(self, request, *args, **kwargs):
    #     fine_rate = 2
    #     current_date=date.today()
    #     borrowData=BorrowModel.objects.all()
    #     for borrow in borrowData:
    #         days_overdue = (current_date - borrow.date_of_return).days
    #         if days_overdue > 0:
    #             fine_amount = fine_rate * days_overdue
    #             borrow.fine = fine_amount
    #         else:
    #             borrow.fine = 0
    #         borrow.save()
    #     return super().list(request, *args, **kwargs)

        
    def calculate_fine(self, borrow_instance):
        current_date=date.today()
        days_overdue = (current_date - borrow_instance.date_of_return).days
        fine_per_day = 2  # Adjust this to your fine policy
        if days_overdue > 0 and borrow_instance.returned is False:
            fine_amount = max(0, days_overdue * fine_per_day)
        else:
            fine_amount=0
        return fine_amount

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Calculate and update the fine for each instance in the queryset
        for instance in queryset:
            instance.fine = self.calculate_fine(instance)
            instance.save()

        ser = self.get_serializer(queryset, many=True)
        return Response(data=ser.data)
